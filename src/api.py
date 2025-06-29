import requests
import json

from src.constants import *
from urllib.parse import urlencode


def get_address_coordinates(address):
    if not address:
        return ['ERROR: address connot be empty']

    params = encode_params({'key': API_KEY})
    url = f"{HOST}/search/{V2}/geocode/{address}.json?{params}"
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        latitude = data["results"][0]["position"]["lat"]
        longitude = data["results"][0]["position"]["lon"]
        return latitude, longitude
    except Exception as e:
        return [f"ERROR: Unable to retrive coordinates: {e}"]


def get_directions(src, dst):
    params = encode_params(
        {
            'instructionsType': 'text',
            'language': 'en-GB',
            'key': API_KEY
        }
    )
    url = f"{HOST}/routing/{V1}/calculateRoute/{src[0]},{src[1]}:{dst[0]},{dst[1]}/json?{params}"
    directions = []
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        instructions = data['routes'][0]['guidance']['instructions']
        for i, instruction in enumerate(instructions):
            directions.append(f'{i + 1}. {instruction['message']}')
        return directions
    except Exception as e:
        return [f"ERROR: Unable to retrive directions: {e}"]


def encode_params(params):
    return urlencode(params)
