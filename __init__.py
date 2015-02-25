# coding: cp1251
class Account(object):
    def __init__(self, accnum, bic):
        self.dict_cl_acc = {'A': '0', 'А': '0',
                            'B': '1', 'В': '1',
                            'C': '2', 'С': '2',
                            'E': '3', 'Е': '3',
                            'H': '4', 'Н': '4',
                            'K': '5', 'К': '5',
                            'M': '6', 'М': '6',
                            'P': '7', 'Р': '7',
                            'T': '8', 'Т': '8',
                            'X': '9', 'Х': '9'}
        self.accnum = str(accnum)
        self.bic = bic
        self.rkcnum = "0" + self.bic[4:6]
        self.key = self.accnum[8:9]
        self.currency = self.accnum[5:6]
        # self.normaccnum = self.rkcnum + self.accnum[0:8] + "0" + self.accnum[9:20]

        self.normaccnum = self.accnum[0:8] + "0" + self.accnum[9:20]

        if self.currency in self.dict_cl_acc:
            self.normaccnum = self.normaccnum.replace(self.currency, self.dict_cl_acc[self.currency])
        self.normaccnum = self.rkcnum + self.normaccnum

    def calcacckey(self):
        mask = "71371371371371371371371"
        summ = 0
        for i in range(len(self.normaccnum)):
            # print self.accnum[i], mask[i], str(int(self.accnum[i]) * int(mask[i]))
            summ += int(self.normaccnum[i]) * int(mask[i])
        print("Summ : {0}".format(str(summ)))


acc1 = Account("40702Е99700000000010", "044579203")
print("accnum ", acc1.accnum)
print("normaccnum", acc1.normaccnum)
print("bic", acc1.bic)
print("key", acc1.key)
print("currency", acc1.currency)
print("rkcnum", acc1.rkcnum)
print("dict B lat", acc1.dict_cl_acc["В"])

acc1.calcacckey()
