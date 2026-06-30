from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_pdf(image_name, prediction, confidence, recommendation):

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{image_name}_report.pdf"

    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold",18)
    c.drawString(50,750,"AI Powered Smart Cable Quality Inspection")

    c.setFont("Helvetica",12)

    c.drawString(50,710,f"Date : {datetime.now().strftime('%d-%m-%Y %H:%M')}")

    c.drawString(50,680,f"Image : {image_name}")

    c.drawString(50,650,f"Prediction : {prediction}")

    c.drawString(50,620,f"Confidence : {confidence}%")

    c.drawString(50,590,f"Recommendation : {recommendation}")

    c.save()

    return filename