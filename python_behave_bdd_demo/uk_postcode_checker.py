import requests
from urllib.parse import quote

from requests import RequestException


def search_town_from_postcode_double(postcode: str):
    if postcode == "SW1A 2AA":
        return "Westminster"
    elif postcode == "No Such Postcode":
        return "Invalid postcode"


def search_postal_town(postcode: str):
    postcode_result = get_postcode(url="https://api.postcodes.io/postcodes/",
                                   path_param=postcode,
                                   ssl_verify=False)
    status_code = postcode_result["status"]
    if status_code == 200:
        postal_town = postcode_result["result"]["admin_district"]
        return postal_town
    elif status_code == 404:
        return postcode_result["error"]
    else:
        return postcode_result


def get_postcode(url: str, path_param: str, ssl_verify: bool):
    _param = quote(path_param)
    try:
        response = requests.get(url=url + _param, verify=ssl_verify)
        return response.json()
    except RequestException as err:
        return err.response
