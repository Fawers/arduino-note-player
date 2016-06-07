from frequencies import get_frequency


class Note:
    """
    Abstração de uma nota musical.
    """

    def __init__(self, note, length):
        self.note = note.upper()
        self.length = length

    def __str__(self):
        return '%s,%d' % (self.note, self.length)

    def __repr__(self):
        return 'Note(%s)' % str(self)

    def get_milliseconds_for_tempo(self, tempo):
        """
        Para converter a duração da nota em um determinado tempo para
        milisegundos, é necessário dividir 60000 (milisegundos) pelo
        tempo, que nada mais é do que batidas por minuto - batidas para
        cada 60 segundos. Essa conta nos dá o tempo em ms de um quarto
        de nota; dividimos o resultado pela duração (length) da nota
        (inteira, meia, quarto, oitavo, ...) para adquirir a duração
        final desta nota em milisegundos.
        """
        millis = 60000 / tempo
        return millis * 4 / self.length

    def to_arduino(self, tempo):
        """
        Retorna a string a ser enviada para o Arduino. Se esta nota é
        representada pela tupla (nome da nota, duração da nota), no
        Arduino esta mesma nota é representada pela tupla
        (frequência do som, tempo em ms).
        """
        return '%d,%d' % (get_frequency(self.note),
                          self.get_milliseconds_for_tempo(tempo))
