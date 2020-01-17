class GetAllUsers(object):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self):
        users = self.user_repo.get_all()
        return [u.to_dict() for u in users]

class GetUserDetail(object):
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self, user_id):
        user = self.user_repo.get_by_id(user_id)

        if user is None:
            return None
        else:
            userDict = user.to_dict()
            return userDict
    
