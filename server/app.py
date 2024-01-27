from flask import Flask, jsonify
from api import trefle

app = Flask(__name__)

@app.route('/api/plants')
def plants():
    plants_data = trefle.get_plants()
    return jsonify(plants_data)

@app.route('/api/plants/<int:plant_id>')
def plant_details(plant_id):
    plant_data = trefle.get_plant_details(plant_id)
    return jsonify(plant_data) if plant_data else ('', 404)

if __name__ == '__main__':
    app.run(debug=True)
