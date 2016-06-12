from datetime import datetime, timedelta


class User:
    def __init__(self, name, id, tempo):
        self.name = name
        self.id = id
        self.tempo = tempo

    def __eq__(self, other):
        return self.id == other.id

    def get_remaining_seconds(self, total_time, current_timestamp):
        now = datetime.now().timestamp()
        offset = now - current_timestamp

        if offset >= total_time:
            return 0

        return total_time - offset



def create_user(name, id, tempo=120):
    return User(name, id, tempo)
