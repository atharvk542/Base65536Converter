from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the scripts directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

# Import the encode and decode functions
from scripts.encode import encode_to_base65536
from scripts.decode import decode_from_base65536

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/encode", methods=["POST"])
def encode():
    try:
        data = request.get_json()
        text = data.get("encode_input", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        result = encode_to_base65536(text)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/decode", methods=["POST"])
def decode():
    try:
        data = request.get_json()
        encoded_text = data.get("decode_input", "")

        if not encoded_text:
            return jsonify({"error": "No encoded text provided"}), 400

        result = decode_from_base65536(encoded_text)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    number = float(data["number"])
    return jsonify({"result": number})


if __name__ == "__main__":
    app.run(debug=True)
