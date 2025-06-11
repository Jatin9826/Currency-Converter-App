# currency.py
import requests

class Currency:
    def __init__(self, from_currency, to_currency, amount, converted_amount, rate, date):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.converted_amount = converted_amount  # direct from API
        self.rate = rate
        self.date = date
        self.inverse_rate = 1 / rate if rate != 0 else 0

    def format_result(self):
        return (
            f"On {self.date}, {self.amount} {self.from_currency} = "
            f"{self.converted_amount:.2f} {self.to_currency} (Rate: {self.rate:.4f})"
        )

    def reverse_rate(self):
        self.inverse_rate = 1 / self.rate if self.rate != 0 else 0


def check_valid_currency(currency_code):
    url = "https://api.frankfurter.app/currencies"
    response = requests.get(url)
    if response.status_code != 200:
        return False
    return currency_code.upper() in response.json()


def extract_api_result(data):
    """
    Parses Frankfurter API result and returns a Currency object.
    Assumes input data structure:
    {
        'amount': 10.0,
        'base': 'USD',
        'date': '2023-06-11',
        'rates': {'INR': 83.01}
    }
    """
    from_currency = data['base']
    amount = float(data['amount'])
    date = data['date']
    to_currency = list(data['rates'].keys())[0]
    rate = data['rates'][to_currency]
    converted_amount = rate  # This already includes the amount, as rate is scaled

    return Currency(from_currency, to_currency, amount, converted_amount, rate / amount, date)
