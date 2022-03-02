import abc


class BillServiceInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBill(self, Id, groupId, amount, contribution, paidBy):
        pass
