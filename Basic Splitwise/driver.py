from controller.bill_controller import BillController
from controller.group_controller import GroupController
from controller.user_controller import UserController
from service.bill_service import BillService
from service.user_service import UserService
from service.group_service import GroupService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser("user1", "user1")
user2 = userController.addUser('user2', 'user2')
user3 = userController.addUser('user3', 'user3')
user4 = userController.addUser('user4', 'user4')

members = [user1, user2, user3, user4]

group1 = groupController.addGroup('group1', 'flatmate', members)

paidby = {'user1': 300, 'user3': 200}
contribution = {'user1': 100, 'user2': 100, 'user3': 100, 'user4': 100}

bill = billController.addBill('bill1', 'group1', 500, contribution, paidby)
print(billController.getUserBalance('user1'))
print(billController.getUserBalance('user2'))
print(billController.getUserBalance('user3'))
print(billController.getUserBalance('user4'))
