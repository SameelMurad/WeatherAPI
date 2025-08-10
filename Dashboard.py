import streamlit as st
import pandas as pd

df = pd.read_csv("weather_data.csv")


def coat_rec(df):
    recent = df.loc[df['timestamp'].idxmax()]
    
    if recent['feels_like'] < 10:
        return f"Wear coat, it feels like {recent['feels_like']}"
    elif recent['wind_speed'] > 4:
        return f"Wear coat, wind speeds are {recent['wind_speed']}"
    else:
        return "No need for a coat"

st.title("Weather Coat Recommendation")
st.write(coat_rec(df))
