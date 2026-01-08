from flask import Flask, request, jsonify
from flask_cors import CORS

from speech_recognition import speech_to_text
from nlp_processor import process_text
from sign_mapper import map_to_signs

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return {"status": "Speech-to-Sign Backend Running"}

@app.route("/convert", methods=["POST"])
def convert_text():
    data = request.json
    text = data.get("text", "")

    processed = process_text(text)
    signs = map_to_signs(processed)

    return jsonify({
        "original_text": text,
        "processed_text": processed,
        "signs": signs
    })

@app.route("/speech", methods=["GET"])
def convert_speech():
    text = speech_to_text()
    processed = process_text(text)
    signs = map_to_signs(processed)

    return jsonify({
        "original_text": text,
        "processed_text": processed,
        "signs": signs
    })

if __name__ == "__main__":
    app.run(debug=True)
