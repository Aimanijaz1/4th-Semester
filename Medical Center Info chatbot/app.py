from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
from Medical_pairs import medical_pairs
import random

app = Flask(__name__)
chatbot = Chat(medical_pairs, reflections)

default = [
    "I didn't understand what you are talking about?",
    "I didn't quite get that.",
    "Can you give me more details that what you want to know about?"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def reply():
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"response": "Please enter a message."})  # changed 'reply' to 'response'
    
    reply = chatbot.respond(user_input.lower())
    if not reply:
        reply = random.choice(default)

    return jsonify({"response": reply})  # changed 'reply' to 'response'

if __name__ == "__main__":
    app.run(debug=True)
