# Músicas de exemplo para o bot


class Song:
    """
    Abstração de uma música.
    """

    def __init__(self, name, tempo, sequence):
        self.name = name
        self.tempo = tempo
        self.seq = sequence


songs = [
    Song('Metal Gear Solid - Main Theme', 100,
           'fs5,2 e5,2 d5,2 d5,8 e5,8 fs5,8 b4,8 fs5,4 e5,2 d5,8 e5,8 '
           'fs5,2 fs5,8 b5,8 a5,8 fs5,8 d5,4 e5,2 fs4,8 b4,8 d5,2 d5,8 '
           'cs5,8 d5,8 e5,8 d5,4 b4,2 a4,8 b4,8 cs5,4 cs5,8 d5,8 cs5,4 '
           'b4,8 a4,8 b4,1'),
    Song('Explosions In The Sky - A Song For Our Fathers', 84,
           'b4,8 b4,8 d6,8 b4,8 d5,8 d5,8 fs6,8 d5,8 a4,8 fs6,8 b5,8 '
           'g5,8 e6,8 b5,8 g5,8 b5,8 g5,16 e5,16 e5,8 d6,8 e5,8 b4,8 '
           'd6,8 cs6,8 b4,8 g5,8 g5,8 d6,8 a5,8 d6,8 cs6,8 a5,8 cs6,8 '
           'b4,8 b4,8 d6,8 b4,8 d5,8 d5,8 fs6,8 d5,8 a4,8 fs6,8 b5,8 '
           'g5,8 e6,8 b5,8 g5,8 b5,8 g5,16 e5,16 e5,8 d6,8 e5,8 b4,8 '
           'd6,8 cs6,8 b4,8 g5,8 g5,8 d6,8 a5,8 d6,8 e6,8 cs6,8 a5,8'),
    Song('The Legend of Zelda - Song of Storms', 100,
           'b4,16 fs5,16 b5,4 b4,16 fs5,16 b5,4 cs6,8 cs6,16 d6,16 '
           'cs6,16 d6,16 cs6,16 a5,16 fs5,4 fs5,8 b4,8 d5,16 e5,16 '
           'fs5,4 fs5,8 fs5,8 b4,8 d5,16 e5,16 cs5,4 cs5,8 '
           'b4,16 fs5,16 b5,4 b4,16 fs5,16 b5,4 cs6,8 cs6,16 d6,16 '
           'cs6,16 d6,16 cs6,16 a5,16 fs5,4 fs5,8 b4,8 d5,16 e5,16 '
           'fs5,4 fs5,8 b4,2'),
    Song('Pantera - Cowboys from Hell', 120,
           'e4,16 g4,16 e4,16 g4,16 a4,16 g4,16 a4,16 g4,16 as4,16 '
           'g4,16 a4,16 g4,16 a4,16 as4,16 d5,8 e4,16 g4,16 e4,16 '
           'g4,16 a4,16 g4,16 a4,16 g4,16 as4,16 g4,16 a4,16 g4,16 '
           'a4,16 as4,16 d5,8 e4,16 g4,16 e4,16 g4,16 a4,16 g4,16 '
           'a4,16 g4,16 as4,16 g4,16 a4,16 g4,16 a4,16 as4,16 d5,8 '
           'e4,16 g4,16 e4,16 g4,16 a4,16 g4,16 a4,16 g4,16 as4,16 '
           'a4,16 g4,16 e4,4 '
           'e5,16 g5,16 e5,16 g5,16 a5,16 g5,16 a5,16 g5,16 as5,16 '
           'g5,16 a5,16 g5,16 a5,16 as5,16 d6,8 e5,16 g5,16 e5,16 '
           'g5,16 a5,16 g5,16 a5,16 g5,16 as5,16 g5,16 a5,16 g5,16 '
           'a5,16 as5,16 d6,8 e5,16 g5,16 e5,16 g5,16 a5,16 g5,16 '
           'a5,16 g5,16 as5,16 g5,16 a5,16 g5,16 a5,16 as5,16 d6,8 '
           'e5,16 g5,16 e5,16 g5,16 a5,16 g5,16 a5,16 g5,16 as5,16 '
           'a5,16 g5,16 e5,4')
]
