import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'


def call_api(url: str):
    """
    Calls the specified API endpoint and returns the response if successful.

    Parameters
    ----------
    url : str
        URL of the API endpoint.

    Returns
    -------
    requests.models.Response or None
        Response object if successful, otherwise None.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            print("There is an error with API call")
            return None
    except requests.exceptions.RequestException as e:
        print(f"API call failed: {e}")
        return None


def format_currencies_url() -> str:
    """
    Formats the URL for the currencies endpoint.

    Returns
    -------
    str
        Formatted URL.
    """
    return _HOST_ + _CURRENCIES_


def get_currencies():
    """
    Extracts currency codes available from the Frankfurter app.

    Returns
    -------
    list
        List of currency codes or empty list on error.
    """
    response = call_api(format_currencies_url())
    if response:
        dict_currency = response.json()
        return list(dict_currency.keys())
    return []


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Formats the URL for the latest conversion rate between two currencies.

    Parameters
    ----------
    from_currency : str
    to_currency : str

    Returns
    -------
    str
        Formatted URL.
    """
    return f"{_HOST_}{_LATEST_}?from={from_currency}&to={to_currency}"
