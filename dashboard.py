import streamlit as st
import plotly.express as px
import pandas as pd

def show_dashboard(predictions):

    st.header("📊 Dashboard")

    if len(predictions) == 0:
        st.info("No predictions yet.")
        return

    df = pd.DataFrame(predictions)

    st.metric("Total Predictions", len(df))

    fig = px.pie(
        df,
        names="Prediction",
        title="Good vs Damaged"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        df,
        x=df.index,
        y="Confidence",
        color="Prediction",
        title="Prediction Confidence"
    )

    st.plotly_chart(fig2, use_container_width=True)