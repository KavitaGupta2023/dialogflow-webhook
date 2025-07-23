from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req_data = request.get_json()
    tag = req_data.get('fulfillmentInfo', {}).get('tag')

    if tag == 'get_efilling':
        try:
            # Call the public weather API
            efilling_res = requests.get('https://www.incometax.gov.in/iec/foportal/')
            efilling_text = efilling_res.text.strip()

            return jsonify({
                "fulfillment_response": {
                    "messages": [
                        {
                            "text": {
                                "text": [f"Here's the efilling info: {efilling_text}"]
                            }
                        }
                    ]
                }
            })
        except Exception as e:
            return jsonify({
                "fulfillment_response": {
                    "messages": [
                        {
                            "text": {
                                "text": ["Sorry, couldn't get the efiiling information."]
                            }
                        }
                    ]
                }
            })

    # Default response for unknown tags
    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": ["Sorry, I couldn't handle that request."]
                    }
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(port=8080, debug=True)

