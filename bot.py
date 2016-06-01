import re

import telepot

from user import create_user


# Constantes - comandos

LOCK_COMMAND_PATTERN = re.compile(r'^/lock$')

NOTES_COMMAND_PATTERN = re.compile(r'^/notas$')

TEMPO_COMMAND_PATTERN = re.compile(r'^/tempo (\d+)$')


# Auxiliares - gerenciamento de usuários

user_queue = []

current_user = None


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

    # O faz somente se a fila não estiver vazia.
    if user_queue:
        current_user = user_queue.pop(0)


def process_message(msg, user):
    """
    Aqui ocorre o processamento de fato das mensagens. No momento em que
    o programa chega aqui, já é garantido que o user é o usuário atual.
    Checa-se se a mensagem é algum dos comandos; se não for, tenta
    parsear as notas. Se não forem notas, envia uma mensagem de erro ao
    usuário.
    """

    pass


def handle_message(msg):
    """
    Ponto de entrada das mensagens recebidas no Telegram.
    """

    user = create_user(msg['from']['first_name'], msg['from']['id'],
                       msg['date'])

    if user == current_user:
        process_message(msg, user)
    else:
        if enqueue_user(user):
            bot.send_message(user.id, 'Você foi adicionado à fila. '
                                      'Aguarde um instante, por favor.')




