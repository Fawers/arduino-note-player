import re
from time import sleep
from datetime import datetime

import telepot

import arduino
from notes import Note
from user import create_user
from frequencies import get_available_notes


# Constantes - comandos

START_COMMAND_PATTERN = re.compile(r'^/start$')

QUEUE_COMMAND_PATTERN = re.compile(r'^/queue$')

NOTES_COMMAND_PATTERN = re.compile(r'^/notas$')

TEMPO_COMMAND_PATTERN = re.compile(r'^/tempo(?: (\d+))?$')

SERIAL_COMMAND_PATTERN = re.compile(r'^/serial$')

END_COMMAND_PATTERN = re.compile(r'^/end$')

# queue - Entra na fila do tocador de notas
# notas - Exibe as notas disponíveis para tocar
# tempo - Muda o tempo usado para tocar as notas; use /tempo NUMERO
# end - Finaliza a sessão


# Regex de notas de entrada

NOTE_PATTERN = re.compile(r'^[a-gA-G][Ss]?[4-6],\d\d?$')


# Auxiliares - gerenciamento de usuários

user_queue = []

current_user = None

user_timestamp = None


# Bot

bot = telepot.Bot('213263906:AAHcQVnfMKX-DTUemItV1P-3sOQwuGhLPCQ')


# Funções

def enqueue_user(user):
    """
    Coloca o usuário no final da fila se ele já não estiver presente na
    mesma.
    """

    if user not in user_queue:
        user_queue.append(user)
        return True

    return False


def shift_users():
    """
    Define o próximo usuário na fila como usuário atual. Isso
    possibilita o usuário a enviar comandos e notas.
    """

    global current_user
    global user_timestamp

    # O faz somente se a fila não estiver vazia.
    if user_queue:
        current_user = user_queue.pop(0)
        user_timestamp = datetime.now().timestamp()
        bot.sendMessage(
            current_user.id,
            current_user.name +
            ', você está no comando agora. 1 minuto de inatividade resultará '
            'na abdicação do controle.')
        bot.sendMessage(
            current_user.id, 'Para finalizar a sessão, use o comando /end.')


def process_message(msg, user):
    """
    Aqui ocorre o processamento de fato das mensagens. No momento em que
    o programa chega aqui, já é garantido que o user é o usuário atual.
    Checa-se se a mensagem é algum dos comandos; se não for, tenta
    parsear as notas. Se não forem notas, envia uma mensagem de erro ao
    usuário.
    """

    global current_user
    global user_timestamp
    text = msg['text']

    # Em primeiro lugar, atualizar a timestamp do usuário
    user_timestamp = msg['date']

    # Verificar se a mensagem é um dos comandos: end, notas ou tempo

    if NOTES_COMMAND_PATTERN.match(text):
        notes = get_available_notes()

        bot.sendMessage(user.id, 'As notas disponíveis são:')
        bot.sendMessage(user.id, '\n'.join(notes))
        bot.sendMessage(user.id, 'Podem ser escritas em maiúsculo ou minúsculo.')
        return

    elif END_COMMAND_PATTERN.match(text):
        bot.sendMessage(user.id, 'Sessão finalizada.')
        current_user = None
        shift_users()
        return

    m = TEMPO_COMMAND_PATTERN.match(text)
    if m:
        tempo = int(m.groups()[0] or user.tempo)
        user.tempo = tempo
        bot.sendMessage(user.id, 'Tempo: %d' % user.tempo)
        return

    # Neste ponto, o usuário deve ter enviado notas de fato

    note_list = []
    for note in text.split():
        if not NOTE_PATTERN.match(note):
            bot.sendMessage(user.id, 'Nota inválida: ' + note)
            continue

        note, length = note.split(',')
        note_list.append(Note(note, int(length)))

    arduino_notes = ' '.join(n.to_arduino(user.tempo) for n in note_list) + '\n'

    print(note_list)
    print(arduino_notes)

def handle_message(msg):
    """
    Ponto de entrada das mensagens recebidas no Telegram.
    """

    user = create_user(msg['from']['first_name'], msg['from']['id'])

    if START_COMMAND_PATTERN.match(msg['text']):
        bot.sendMessage(
            user.id,
            'Olá, %s! Bem-vindo ao programa tocador de notas do Arduino. '
            'Use o comando /queue para entrar na fila.' % user.name)
        bot.sendMessage(
            user.id,
            'O comando /tempo N serve para mudar o tempo em BPM das notas '
            'que serão tocadas.\nPara mandar tocar as notas de fato, envie '
            'NOTA,DURAÇÃO. Pode enviar quantas quiser de uma só vez. Exemplo:')
        m = bot.sendMessage(
            user.id,
            'fs5,2 e5,2 d5,2 d5,8 e5,8 fs5,8 b4,8 fs5,4 e5,2 d5,8 e5,8 '
            'fs5,2 fs5,8 b5,8 a5,8 fs5,8 d5,4 e5,2 fs4,8 b4,8 d5,2 d5,8 '
            'cs5,8 d5,8 e5,8 d5,4 b4,2 a4,8 b4,8 cs5,4 cs5,8 d5,8 cs5,4 '
            'b4,8 a4,8 b4,1')
        bot.sendMessage(
            user.id,
            'Este é o tema principal da franquia Metal Gear Solid.',
            reply_to_message_id=m['message_id'])

        return

    elif SERIAL_COMMAND_PATTERN.match(msg['text']):
        for i in range(100):
            if arduino.setup_serial():
                bot.sendMessage(user.id, 'Serial reconfigurada.')
                break
        else:
            bot.sendMessage(user.id, 'Não foi possível reconfigurar a serial.')

        return

    if current_user is not None and user.id == current_user.id:
        process_message(msg, current_user)

    else:
        # Verifica se o comando é de enfileirar
        if QUEUE_COMMAND_PATTERN.match(msg['text']):
            if enqueue_user(user):
                if len(user_queue) == 1 and current_user is None:
                    shift_users()
                else:
                    bot.sendMessage(user.id, 'Você foi adicionado à fila. '
                                             'Aguarde um instante, por favor.')
            else:
                bot.sendMessage(user.id, 'Você já está na fila.')




if __name__ == '__main__':
    bot.message_loop(handle_message)
    print('main loop started')

    while True:
        sleep(10)
