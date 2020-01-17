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
        return self.question_repo.create(question_text, user_id).to_dict()


class GetAllQuestionsUseCase(object):
    def __init__(self, question_repo):
        self.question_repo = question_repo

    def execute(self):
        questions = self.question_repo.get_all()
        return [q.to_dict() for q in questions]
    

class FetchQuestionUseCase(object):
    def __init__(self, question_repo):
        self.question_repo = question_repo

    def execute(self, question_id):
        question = self.question_repo.get_by_id(question_id)
        return question.to_dict()
    
    
class AnsweringQuestionUseCase(object):
    def __init__(self, answer_repo):
        self.answer_repo = answer_repo

    def execute(self, answer_text, user_id, question_id):
        new_answer = self.answer_repo.create(answer_text, user_id, question_id)
        return new_answer.to_dict()


class GetAllAnswersUseCase(object):
    def __init__(self, answer_repo):
        self.answer_repo = answer_repo

    def execute(self):
        answers = self.answer_repo.get_all()
        return [a.to_dict() for a in answers]
