from flask import Flask
from dotenv import load_dotenv
from config import Config

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)

# Define routes
@app.route('/')
def index():
    return "Hello, World!"


def process_garden(beds):
    """Calculates garden area and sunlight"""
    total_area = 0
    sunny_area = 0
    
    for bed in beds:
        length = bed['length']
        width = bed['width']
        area = length * width  # Calculate bed area
        total_area += area 
        
        if bed['sunlight'] == 'sunny':
            sunny_area += area
            
    if sunny_area / total_area > 0.5:
        garden_sun = 'sunny'
    else:
        garden_sun = 'shade'
        
    return total_area, garden_sun 

def get_plant_recs(zone, garden_sun, total_area):
    """Returns plant recommendations based on inputs"""
    # Query the Trefle API for plants in the zone, filter by garden_sun
    response = ...  
    
    # Further filter plants based on growth habit to exclude large plants
    # that won't fit in the specified garden area. 
    
    # Return a list of recommended plants with details like:
    # - Planting times
    # - Care needs (water, nutrients, pruning)
    # - Growth habit (height, spread)
    recs = []
    for plant in response: 
        if plant['height'] < ... and plant['spread'] < ...:  # Check if fits in area
            rec = {
                'name': plant['scientific_name'],
                'planting': plant['bloom_months'],   # Example - use planting info
                'care': plant['growth']['light'],      # Example - use care info 
                'height': plant['maximum_height'],    # Provide full growth details
                'spread': plant['spread']  
            }
            recs.append(rec)
            
    return recs 

# More route definitions

if __name__ == '__main__':
    app.run(debug=True)