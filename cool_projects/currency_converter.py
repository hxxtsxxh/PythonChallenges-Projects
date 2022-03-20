import requests


class RealTimeCurrencyConverter:
    def __init__(self, link):
        self.amount = None
        self.data = requests.get(link).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        self.amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return str(amount)


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConverter(url)

from_inp = input("Type the three character currency code of the country you are transforming from (all caps): ")
to_inp = input("Type the three character currency code of the country you are transforming to (all caps): ")
the_amt = float(input("Amount you would like to convert: "))
print(converter.convert(from_inp, to_inp, the_amt) + ' ' + to_inp)
