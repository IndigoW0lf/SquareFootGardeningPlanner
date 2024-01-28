```python
import pandas as pd

df = pd.read_csv('zip_zone.csv')  # Load zone lookup dataframe

@app.route('/zones/<zip_code>')
def get_zone(zip_code):
    """Returns the USDA zone for a given zip code"""
    if not zip_code.isdigit() or len(zip_code) != 5:
        abort(400)  # Invalid zip code
    
    zip_code = int(zip_code)
    zone = df.loc[df['zip'] == zip_code, 'zone'].iloc[0]
    
    if not zone:
        abort(404)  # Zone not found
    
    return jsonify({'zone': zone})
```