# from flask import Flask, request, jsonify, render_template
# import requests

# app = Flask(__name__)

# API_KEY = "had3zWY2AWtKx3vorIHlIqojuuiyR0CA"
# BASE_URL = "https://api.mistral.ai/v1/chat/completions"

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_message = request.json.get("message")

#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": "mistral-large-latest",
#         "messages": [
#             {
#                 "role": "system",
#                 "content": """
# You are a strict professional healthcare assistant.
# Rules:
# 1. Answer ONLY medical or healthcare related questions.
# 2. If user asks non-health question, say:
# 'I am a healthcare assistant and can only answer medical-related questions.'
# 3. Always give safe advice.
# 4. Always suggest consulting a doctor for serious symptoms.
# """
#             },
#             {
#                 "role": "user",
#                 "content": user_message
#             }
#         ],
#         "temperature": 0.4
#     }

#     try:
#         response = requests.post(BASE_URL, headers=headers, json=payload)
#         data = response.json()

#         if "choices" in data:
#             reply = data["choices"][0]["message"]["content"] + \
#                     "<br><br>⚠️ This AI does not replace a real doctor."
#         else:
#             reply = "Error getting response from AI."

#         return jsonify({"reply": reply})

#     except Exception as e:
#         return jsonify({"reply": "Server error occurred."})


# if __name__ == "__main__":
#     app.run(debug=True)







from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# API KEY environment variable se read karega
API_KEY = os.environ.get("MISTRAL_API_KEY")

BASE_URL = "https://api.mistral.ai/v1/chat/completions"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-large-latest",
        "messages": [
            {
                "role": "system",
                "content": """
You are a strict professional healthcare assistant.
Rules:
1. Answer ONLY medical or healthcare related questions.
2. If user asks non-health question, say:
'I am a healthcare assistant and can only answer medical-related questions.'
3. Always give safe advice.
4. Always suggest consulting a doctor for serious symptoms.
"""
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
        "temperature": 0.4
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload)
        data = response.json()

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"] + \
                "<br><br>⚠️ This AI does not replace a real doctor."
        else:
            reply = "Error getting response from AI."

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Server error occurred."})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)