from config import Config
from bravado.client import SwaggerClient
from collections import OrderedDict
import hashlib
import logging
from datetime import datetime

# Setting up logging
logging.basicConfig(filename='trefle.log', level=logging.INFO)

# Cache configuration
CACHE_MAX_SIZE = 1000
cache = OrderedDict()

# Swagger client configuration
spec_path = 'server/config/swagger.yaml'
client = SwaggerClient.from_file(spec_path, config={'use_models': True})

# API configuration
TREFLE_API_URL = "https://api.trefle.io/api/v1/plants"
TREFLE_TOKEN = Config.TREFLE_API_TOKEN

# Utility function to generate cache key
def generate_cache_key(plant_id):
    return hashlib.md5(str(plant_id).encode()).hexdigest()

# Function to check and update cache
def check_cache(key):
    if key in cache:
        cache.move_to_end(key)
        logging.info(f"Cache hit for key: {key}")
        return cache[key]
    else:
        logging.info(f"Cache miss for key: {key}")
        return None

# Function to add to cache
def add_to_cache(key, data):
    if len(cache) >= CACHE_MAX_SIZE:
        oldest_key = next(iter(cache))
        cache.pop(oldest_key)
        logging.info(f"Evicted cache key: {oldest_key}")
    cache[key] = data

def get_plant_info(plant_id):
    cache_key = generate_cache_key(plant_id)
    cached_response = check_cache(cache_key)
    if cached_response:
        return cached_response

    try:
        response = client.plants.getPlant(id=plant_id).response()
        plant_data = response.result
        add_to_cache(cache_key, plant_data)
        return plant_data
    except Exception as e:
        logging.error(f"Error fetching plant info: {e}", exc_info=True)
        return None