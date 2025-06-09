from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

@app.route('/')
def home():
    return jsonify({"message": "Instagram Clone Backend Running"})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


