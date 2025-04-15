from flask import Flask, render_template, request, send_file, jsonify
import qrcode
import os
from io import BytesIO
import cv2
import numpy as np
from pyzbar.pyzbar import decode

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_qr():
    text = request.form.get("text")
    if not text:
        return "No text provided", 400

    qr = qrcode.make(text)
    img_io = BytesIO()
    qr.save(img_io, "PNG")
    img_io.seek(0)
    
    return send_file(img_io, mimetype="image/png")

@app.route("/read", methods=["POST"])
def read_qr():
    if "file" not in request.files:
        return jsonify({"decoded_text": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"decoded_text": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    image = cv2.imread(file_path)
    qr_codes = decode(image)
    decoded_text = qr_codes[0].data.decode("utf-8") if qr_codes else "No QR code detected."

    os.remove(file_path)  # Clean up the uploaded file

    return jsonify({"decoded_text": decoded_text})

if __name__ == "__main__":
    app.run(debug=True)
