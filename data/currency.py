import requests

def get_currensy(cur1, cur2):
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{cur1}/{cur2}.json"

    response = requests.get(url).json()

    return response