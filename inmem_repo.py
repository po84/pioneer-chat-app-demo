import uuid
from entities import User

class UserRepo(object):
    def __init__(self):
        self.data_store = {}

    def create(self, display_name):
        id = str(uuid.uuid4())
        user = User(id, display_name)
        self.data_store[id] = user

        return True

    def get_all(self):
        return [user for user in self.data_store.values()]

    def get_by_id(self, user_id):
        if user_id in self.data_store:
            return self.data_store[user_id]
        else:
            return None
