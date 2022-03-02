class BillController(object):
    def __init__(self, BillService):
        self.BillService = BillService

    def addBill(self, Id, groupId, amount, contribution, paidBy):
        return self.BillService.addBill(Id, groupId, amount, contribution, paidBy)

    def getUserBalance(self, userId):
        balance = 0
        for billId in self.BillService.billData:
            bill = self.BillService.billData[billId]
            if userId in bill.getContribution():
                balance = balance - bill.getContribution()[userId]
            if userId in bill.getPaidBy():
                balance = balance + bill.getPaidBy()[userId]
        return balance

