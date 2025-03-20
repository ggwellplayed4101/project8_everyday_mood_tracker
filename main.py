import streamlit as st
import plotly.express as px 
from backend import read_mood_of

positivity_indexes, negativity_indexes, dates = read_mood_of()
st.title("Diary Tone")

st.subheader("Positivity")
figure1 = px.line(y=positivity_indexes, x=dates,
                 labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure1)

st.subheader("Negativity")
figure2 = px.line(y=negativity_indexes, x=dates,
                 labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure2)