import streamlit as st
import plotly.express as px 

st.title("Diary Tone")
st.subheader("Positivity")
figure = px.line(y=[1,8,3], x=[2023,2024,2025],
                 labels={"x": "Date", "y": "Positivity"})

st.plotly_chart(figure)