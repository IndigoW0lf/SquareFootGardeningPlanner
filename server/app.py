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

# More route definitions

if __name__ == '__main__':
    app.run(debug=True)