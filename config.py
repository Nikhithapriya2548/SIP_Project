import os

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "cable_model.keras")

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

ASSET_FOLDER = os.path.join(BASE_DIR, "assets")

IMAGE_SIZE = (224, 224)

CLASS_NAMES = [
    "Damaged",
    "Good"
]

CONFIDENCE_THRESHOLD = 0.60

APP_TITLE = "AI Powered Smart Cable Quality Inspection System"

APP_ICON = "🔌"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(REPORT_FOLDER):
    os.makedirs(REPORT_FOLDER)