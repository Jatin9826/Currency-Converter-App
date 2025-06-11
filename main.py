import sys
from api import call_api, format_latest_url
from currency import check_valid_currency, extract_api_result


def main():
    """
    Entry point of the Currency Converter application.
    Validates command-line arguments and initiates conversion.
    """
    args = sys.argv[1:]

    if len(args) == 2:
        get_rate(args[0], args[1])
    elif len(args) < 2:
        print("[ERROR] You haven't provided 2 currency codes")
    else:
        print("[ERROR] You have provided more than 2 currency codes")


def get_rate(from_currency: str, to_currency: str):
    """
    Validates currency codes, fetches the latest exchange rate, and prints the result.

    Parameters
    ----------
    from_currency : str
    to_currency : str
    """
    from_check = check_valid_currency(from_currency)
    to_check = check_valid_currency(to_currency)

    if from_check and to_check:
        api_url = format_latest_url(from_currency, to_currency)
        response = call_api(api_url)
        if response:
            currency = extract_api_result(response.json())
            print(currency.format_result())
    elif from_check:
        print(f"[ERROR] {to_currency} is not a valid currency code")
    elif to_check:
        print(f"[ERROR] {from_currency} is not a valid currency code")
    else:
        print(f"[ERROR] Both {from_currency} and {to_currency} are invalid currency codes")


if __name__ == "__main__":
    main()
