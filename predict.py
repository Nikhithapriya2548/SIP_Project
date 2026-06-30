import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

from utils import preprocess_image

# Build the same model architecture
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)
x = Dense(128, activation="relu")(x)
output = Dense(1, activation="sigmoid")(x)

model = Model(base_model.input, output)

# Load weights
model.load_weights("model/cable_model.weights.h5")


def predict_image(image):
    img = preprocess_image(image)

    prediction = model.predict(img, verbose=0)[0][0]

    confidence = round(max(prediction, 1 - prediction) * 100, 2)

    if prediction >= 0.5:
        return "Good", confidence, "Cable is safe to use."
    else:
        return "Damaged", confidence, "Replace or inspect the cable."
