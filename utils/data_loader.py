import pandas as pd
import streamlit as st

@st.cache_data
def load_and_clean_data(file_path="data/public_health_data.csv"):
    df = pd.read_csv(file_path)
    # Basic data hygiene checks
    df['GDP_per_Capita'] = pd.to_numeric(df['GDP_per_Capita'], errors='coerce')
    df['LifeExpectancy'] = pd.to_numeric(df['LifeExpectancy'], errors='coerce')
    return df
