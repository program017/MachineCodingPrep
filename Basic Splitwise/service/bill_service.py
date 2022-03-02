from model.bill_model import Bill
from service.bill_service_interface import BillServiceInterface


class BillService(BillServiceInterface):
    billData = {}

    def addBill(self, Id, groupId, amount, contribution, paidBy):
        bill = Bill()
        bill.setId(Id)
        bill.setGroupId(groupId)
        bill.setAmount(amount)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billData[Id] = bill
        return bill
