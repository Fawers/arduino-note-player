from collections import namedtuple


User = namedtuple('name', 'id', 'last_message', 'tempo')


def create_user(name, id, last_message, tempo=120):
    return User(name, id, last_message, tempo)
