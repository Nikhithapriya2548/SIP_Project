import numpy as np
from tensorflow.keras.models import load_model
from utils import preprocess_image

MODEL_PATH = "model/cable_model.keras"

model = load_model(MODEL_PATH)

def predict_image(image):

    img = preprocess_image(image)

    prediction = model.predict(img, verbose=0)[0][0]

    confidence = round(max(prediction, 1 - prediction) * 100, 2)

    if prediction >= 0.5:
        label = "Good"
        recommendation = "Cable is safe to use."
    else:
        label = "Damaged"
        recommendation = "Replace or inspect the cable."

    return label, confidence, recommendation