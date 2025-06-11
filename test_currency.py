import unittest
from currency import check_valid_currency, Currency


class TestValidCurrency(unittest.TestCase):

    def test_valid_currency(self):
        # Common valid currency code
        self.assertTrue(check_valid_currency("USD"))

    def test_invalid_currency(self):
        # Non-existent currency code
        self.assertFalse(check_valid_currency("XYZ"))


class TestCurrencyClass(unittest.TestCase):

    def setUp(self):
        # Sample currency data
        self.currency = Currency(
            from_currency="USD",
            to_currency="GBP",
            amount=1,
            rate=0.72282,
            inverse_rate=0,
            date="2021-09-16"
        )

    def test_attributes(self):
        self.assertEqual(self.currency.from_currency, "USD")
        self.assertEqual(self.currency.to_currency, "GBP")
        self.assertEqual(self.currency.amount, 1)
        self.assertEqual(self.currency.rate, 0.72282)
        self.assertEqual(self.currency.date, "2021-09-16")

    def test_reverse_rate_calculation(self):
        self.currency.reverse_rate()
        expected_inverse = round(1 / self.currency.rate, 5)
        self.assertEqual(self.currency.inverse_rate, expected_inverse)

    def test_format_result(self):
        self.currency.reverse_rate()
        result = self.currency.format_result()
        expected_start = f"Today's ({self.currency.date}) conversion rate from USD to GBP is {self.currency.rate}."
        self.assertIn("conversion rate from USD to GBP", result)
        self.assertIn("inverse rate is", result)


if __name__ == '__main__':
    unittest.main()
