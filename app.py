import streamlit as st
from PIL import Image
import os

from predict import predict_image
from dashboard import show_dashboard
from report import generate_pdf

st.set_page_config(
    page_title="AI Smart Cable Inspection",
    page_icon="🔌",
    layout="wide"
)

st.title("🔌 AI Powered Smart Cable Quality Inspection System")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Inspect Cable",
        "Dashboard"
    ]
)

if "predictions" not in st.session_state:
    st.session_state.predictions=[]

if menu=="Inspect Cable":

    uploaded_file = st.file_uploader(
        "Upload Cable Image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(image,width=450)

        if st.button("Inspect Cable"):

            with st.spinner("Inspecting..."):

                prediction,confidence,recommendation = predict_image(image)

            if prediction=="Good":

                st.success("✅ GOOD CABLE")

            else:

                st.error("❌ DAMAGED CABLE")

            st.metric("Confidence",f"{confidence}%")

            st.write("Recommendation")

            st.info(recommendation)

            st.session_state.predictions.append({

                "Prediction":prediction,

                "Confidence":confidence

            })

            filename=os.path.splitext(uploaded_file.name)[0]

            pdf=generate_pdf(

                filename,

                prediction,

                confidence,

                recommendation

            )

            with open(pdf,"rb") as f:

                st.download_button(

                    "Download Report",

                    f,

                    file_name=os.path.basename(pdf),

                    mime="application/pdf"

                )

elif menu=="Dashboard":

    show_dashboard(st.session_state.predictions)