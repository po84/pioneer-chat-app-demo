class User(object):
    def __init__(self, id, display_name):
        self.id = id
        self.display_name = display_name

    def to_dict(self):
        return {
            'id': self.id,
            'display_name': self.display_name
        }
