import uuid
from entities import User, Question

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


class QuestionRepo(object):
    def __init__(self):
        self.data_store = {}

    def create(self, text, user_id):
        id = str(uuid.uuid4())
        question = Question(id, text, user_id)
        self.data_store[id] = question

        return True

    def get_all(self):
        return [question for question in self.data_store.values()]
