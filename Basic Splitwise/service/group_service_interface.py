import abc


class GroupServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addGroup(self, Id, name, members):
        pass
