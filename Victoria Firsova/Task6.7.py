"""не готовоTask 4.7. Implement a class Money to represent value and currency.
 You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, 
 addition and subtraction). Tip: use class attribute exchange rate which is dictionary and stores information 
 about exchange rates to your default currency:"""

class Money:

    def __init__(self, amount, currency='EUR'):
        self.amount = amount
        self.currency = currency
        self.other_amount = 0
        self.exchange_rate = {
            'EUR': 1,
            'USD': 1.16,
            'BYN': 2.86,
            'RUB': 83,
            'JPY': 131.58,
        }

    def __eq__(self, other):
        self.other_amount = other.amount / other.exchange_rate[other.currency] * self.exchange_rate[self.currency]
        return self.amount == self.other_amount

    def __truediv__(self, other):
        if isinstance(other, (int, float)) :
            self.amount = self.amount / other
            return Money(self.amount, self.currency)

    def __mul__(self, other):
        if isinstance(other,(int,float)):
            self.amount = other * self.amount
            return Money(self.amount, self.currency)

    def __add__(self, other):
        if other.currency != self.currency:
            self.amount = round((self.amount / self.exchange_rate[self.currency] *
                                 other.exchange_rate[other.currency]), 2)
            self.currency = other.currency
            self.amount = other.amount+self.amount
            return Money(self.amount, self.currency)

    def __sub__(self, other):
        if other.currency != self.currency:
            self.amount = round((self.amount / self.exchange_rate[self.currency] *
                                 other.exchange_rate[other.currency]), 2)
            self.currency = other.currency
            self.amount = other.amount - self.amount
            return Money(self.amount, self.currency)

    def __repr__(self) :
        return f'{self.amount} {self.currency}'

x = Money(10, "BYN")
y = Money(11)
z = Money(12.34, "EUR")

print(z +x * 3.11 + y * 0.8) # result in “EUR”


lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = lst[0]+lst[1]+lst[2]
print(s) #result in “BYN”
'''#>>123.45 BYN
'''