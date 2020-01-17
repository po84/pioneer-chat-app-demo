class GetAllUsersUseCase(object):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self):
        users = self.user_repo.get_all()
        return [u.to_dict() for u in users]

class GetUserDetailUseCase(object):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user_id):
        user = self.user_repo.get_by_id(user_id)

        if user is None:
            return None
        else:
            userDict = user.to_dict()
            return userDict
    

class AskQuestionUseCase(object):
    def __init__(self, question_repo):
        self.question_repo = question_repo

    def execute(self, question_text, user_id):
        self.question_repo.create(question_text, user_id)
        return True


class GetAllQuestionsUseCase(object):
    def __init__(self, question_repo):
        self.question_repo = question_repo

    def execute(self):
        questions = self.question_repo.get_all()
        return [q.to_dict() for q in questions]
    
