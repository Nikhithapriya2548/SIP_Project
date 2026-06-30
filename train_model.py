import os
import shutil
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

# ----------------------------
# MVTec Dataset Path
# ----------------------------
MVTEC_PATH = "dataset/cable"

TEMP_DATASET = "dataset_binary"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 5

# ----------------------------
# Create Binary Dataset
# ----------------------------

if os.path.exists(TEMP_DATASET):
    shutil.rmtree(TEMP_DATASET)

os.makedirs(f"{TEMP_DATASET}/train/good", exist_ok=True)
os.makedirs(f"{TEMP_DATASET}/validation/good", exist_ok=True)
os.makedirs(f"{TEMP_DATASET}/validation/damaged", exist_ok=True)

# Copy Good Images

good_train = os.path.join(MVTEC_PATH, "train", "good")

for img in os.listdir(good_train):

    shutil.copy(
        os.path.join(good_train, img),
        os.path.join(TEMP_DATASET, "train", "good", img)
    )

# Copy Test Images

test_path = os.path.join(MVTEC_PATH, "test")

for folder in os.listdir(test_path):

    folder_path = os.path.join(test_path, folder)

    if folder == "good":

        for img in os.listdir(folder_path):

            shutil.copy(
                os.path.join(folder_path, img),
                os.path.join(TEMP_DATASET, "validation", "good", img)
            )

    else:

        for img in os.listdir(folder_path):

            shutil.copy(
                os.path.join(folder_path, img),
                os.path.join(TEMP_DATASET, "validation", "damaged", img)
            )

print("Dataset Prepared Successfully!")

# ----------------------------
# Data Generator
# ----------------------------

train_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

val_gen = ImageDataGenerator(rescale=1./255)

train_data = train_gen.flow_from_directory(
    f"{TEMP_DATASET}/train",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="binary"
)

val_data = val_gen.flow_from_directory(
    f"{TEMP_DATASET}/validation",
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="binary"
)

# ----------------------------
# MobileNetV2
# ----------------------------

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224,224,3)
)

base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)
x = Dense(128, activation="relu")(x)
output = Dense(1, activation="sigmoid")(x)

model = Model(base_model.input, output)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ----------------------------
# Train
# ----------------------------

history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=EPOCHS
)

# ----------------------------
# Save Model
# ----------------------------

os.makedirs("model", exist_ok=True)

model.save("model/cable_model.keras")

print("Model Saved Successfully!")
