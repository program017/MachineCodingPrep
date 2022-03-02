from model.user_model import User
from service.user_service_interface import UserServiceInterface


class UserService(UserServiceInterface):
    userData = {}

    def addUser(self, Id, name):
        user = User()
        user.setId(Id)
        user.setName(name)
        self.__class__.userData[Id] = user
        return user
