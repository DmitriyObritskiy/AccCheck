# -*- coding: utf-8 -*-
class Account(object):

    def __init__(self, accnum):
        self.accnum = str(accnum)

    def checkacckey(self, bic):
        mask = "71371371371371371371371"
        summ = 0
        print len(self.accnum)
        for i in range(len(self.accnum)):
            print self.accnum[i], mask[i], str(int(self.accnum[i]) * int(mask[i]))
            summ += int(self.accnum[i]) * int(mask[i])
            print "Summ = %s", % (summ)

acc1 = Account("40702810100000000010")
print acc1.accnum

acc1.checkacckey("87687")
