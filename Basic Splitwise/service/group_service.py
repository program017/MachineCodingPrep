from model.group_model import Group
from service.group_service_interface import GroupServiceInterface


class GroupService(GroupServiceInterface):
    groupData = {}

    def addGroup(self, Id, name, members):
        group = Group()
        group.setId(Id)
        group.setName(name)
        group.setMembers(members)
        self.__class__.groupData[Id] = group
        return group
