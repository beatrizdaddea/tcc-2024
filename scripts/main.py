import argparse
from PIL import Image

import cv2
import numpy as np
from flask import Flask, request, send_file, Response, jsonify
import os

from ultralytics import YOLO


app = Flask(__name__)

@app.route("/predict_img", methods=["POST"])
def predict_img():
    if 'file' in request.files:
        f = request.files['file']
        # Salvar o arquivo
        filepath = os.path.join('uploads', f.filename)
        f.save(filepath)
        
        # Carregar a imagem
        img = cv2.imread(filepath)

        # Executar a detecção
        model = YOLO('yolov8.pt')
        detections = model(img, save=True) 
        
        # Retornar o nome do arquivo como resultado
        return jsonify({"filename": f.filename})

    return "No file found in request."

# Execução do aplicativo Flask
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov8 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port) 
