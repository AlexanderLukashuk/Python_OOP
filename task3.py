class Currency:
    def __init__(self, currentCurrency, transferCurrency, money):
        self.currentCurrency = currentCurrency
        self.transferCurrency = transferCurrency
        self.money = money

    @property
    def changeCurrency(self):
        if self.currentCurrency == 'Тенге':
            return self.money / 428
        else:
            return self.money * 428

    @money.setter
    def money(self, money):
        self.money = money