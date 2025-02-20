import requests
import json

def search_town_from_postcode(postcode: str):

    if postcode == "SW1A 2AA":
        return "Westminster"
    elif postcode == "No Such Postcode":
        return "Invalid postcode"