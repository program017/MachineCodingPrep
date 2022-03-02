class GroupController(object):
    def __init__(self, GroupService):
        self.GroupService = GroupService

    def addGroup(self, Id, name, members):
        return self.GroupService.addGroup(Id, name, members)
