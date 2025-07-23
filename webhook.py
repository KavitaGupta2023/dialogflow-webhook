from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req_data = request.get_json()
    tag = req_data.get("fulfillmentInfo", {}).get("tag", "")

    if tag == "get_raw_content":
        try:
            # Public URL (can be JSON, HTML, or text)
            public_url = "https://www.incometax.gov.in/iec/foportal/"  # Or any other URL
            response = requests.get(public_url)
            content = response.text.strip()

            # Return the content directly in chatbot message
            return jsonify({
                "fulfillment_response": {
                    "messages": [
                        {
                            "text": {
                                "text": [f"Here's the response:\n{content}"]
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
                                "text": ["Error fetching data."]
                            }
                        }
                    ]
                }
            }), 500

    # Default response if tag doesn't match
    return jsonify({
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": ["No matching webhook tag."]
                    }
                }
            ]
        }
    })

if __name__ == '__main__':
    app.run(port=8080)
