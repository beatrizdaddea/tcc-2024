import argparse
import os
import time
from flask import Flask, request, jsonify, send_from_directory, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('yolov8.pt')

@app.route("/train_and_validate", methods=["GET"])
def train_and_validate():
    dataset_location = import_dataset()
    training_result = train_model(dataset_location)
    return jsonify(training_result)

def import_dataset():
    return "/path/to/dataset"

def train_model(dataset_location):
    return {"status": "success", "message": "Model trained successfully."}

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file found in request."}), 400
    
    f = request.files['file']
    if f.filename == '':
        return jsonify({"error": "No file selected."}), 400
    
    file_extension = f.filename.rsplit('.', 1)[1].lower()
    if file_extension not in ['jpg', 'jpeg', 'png']:
        return jsonify({"error": "Invalid file format. Must be JPG, JPEG, or PNG."}), 400
      
    filepath = os.path.join('uploads', f.filename)
    f.save(filepath)


    prediction_result = predict_image(filepath)
    os.remove(filepath)

    return jsonify(prediction_result)

def predict_image(image_path):
    img = cv2.imread(image_path)

    results = model(img, save=True)

    # Exibir as previsões
    predictions = []
    for image_path in glob.glob("/path/to/predictions/*.jpg"):
        # Adicionar a previsão à lista de resultados
        predictions.append(image_path)

    return {"predictions": predictions}
    # Implemente a lógica para obter frames do vídeo aqui
    while True:
        # Obter frame do vídeo
        frame = cv2.imread("/path/to/video/frame.jpg")

        # Codificar o frame em JPEG
        _, jpeg = cv2.imencode('.jpg', frame)

        # Transmitir o frame
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        time.sleep(0.1)  # Controlar a taxa de quadros

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app for YOLOv8")
    parser.add_argument("--port", default=5000, type=int, help="Port number")
    args = parser.parse_args()
    app.run(host="0.0.0.0", port=args.port)
