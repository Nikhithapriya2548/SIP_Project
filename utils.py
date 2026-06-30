import cv2
import numpy as np
from PIL import Image

IMG_SIZE = (224,224)

def preprocess_image(image):

    image = image.resize(IMG_SIZE)

    img = np.array(image)

    img = img.astype("float32")/255.0

    img = np.expand_dims(img,axis=0)

    return img


def draw_prediction(image,label,confidence):

    img=np.array(image)

    color=(0,255,0)

    if label=="Damaged":
        color=(255,0,0)

    cv2.putText(
        img,
        f"{label} {confidence:.2f}%",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )

    return img