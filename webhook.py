from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get-public-data', methods=['GET'])
def get_public_data():
    try:
        # Replace with your desired public URL
        public_url = "https://www.incometax.gov.in/iec/foportal/"
        response = requests.get(public_url)
        response.raise_for_status()  # Raises error for 4xx/5xx

        data = response.json()
        return jsonify({
            "status": "success",
            "data": data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(port=8080)
