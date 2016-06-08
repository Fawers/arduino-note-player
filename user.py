from collections import namedtuple


class User:
    def __init__(self, name, id, tempo):
        self.name = name
        self.id = id
        self.tempo = tempo

def create_user(name, id, tempo=120):
    return User(name, id, tempo)
