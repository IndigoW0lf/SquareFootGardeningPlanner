import requests
from config import Config

TREFLE_API_URL = "https://api.trefle.io/api/v1/plants"
TREFLE_TOKEN = Config.TREFLE_API_TOKEN


def get_plants(page=1):
    """ Fetch a list of plants """
    response = requests.get(f"{TREFLE_API_URL}?token={TREFLE_TOKEN}&page={page}")
    if response.status_code == 200:
        return response.json()['data']
    else:
        return []

def get_plant_details(plant_id):
    """ Fetch details of a specific plant """
    response = requests.get(f"{TREFLE_API_URL}/{plant_id}?token={TREFLE_TOKEN}")
    if response.status_code == 200:
        return response.json()['data']
    else:
        return None
