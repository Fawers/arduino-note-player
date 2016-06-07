from collections import OrderedDict


frequencies = OrderedDict([
    ('C4', 262),
    ('CS4', 277),
    ('D4', 294),
    ('DS4', 311),
    ('E4', 330),
    ('F4', 349),
    ('FS4', 370),
    ('G4', 392),
    ('GS4', 415),
    ('A4', 440),
    ('AS4', 466),
    ('B4', 494),
    ('C5', 523),
    ('CS5', 554),
    ('D5', 587),
    ('DS5', 622),
    ('E5', 659),
    ('F5', 698),
    ('FS5', 740),
    ('G5', 784),
    ('GS5', 831),
    ('A5', 880),
    ('AS5', 932),
    ('B5', 988),
    ('C6', 1047),
    ('CS6', 1109),
    ('D6', 1175),
    ('DS6', 1245),
    ('E6', 1319),
    ('F6', 1397),
    ('FS6', 1480),
    ('G6', 1568),
    ('GS6', 1661),
    ('A6', 1760),
    ('AS6', 1865),
    ('B6', 1976),
])



def get_frequency(note):
    return frequencies.get(note, None)


def get_available_notes():
    return list(frequencies.keys())
