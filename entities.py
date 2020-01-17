class User(object):
    def __init__(self, id, display_name):
        self.id = id
        self.display_name = display_name

    def to_dict(self):
        return {
            'id': self.id,
            'display_name': self.display_name
        }


class Question(object):
    def __init__(self, id, text, user_id):
        self.id = id
        self.text = text
        self.user_id = user_id

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'user_id': self.user_id,
        }
