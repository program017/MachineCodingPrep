class UserController(object):
    def __init__(self, UserService):
        self.UserService = UserService

    def addUser(self, Id, name):
        return self.UserService.addUser(Id, name)
