import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config('wide')
st.title('Titanic Dasboard')

df = pd.read_csv('titani_data.csv')

df['Embarked'] = df['Embarked'].fillna('Unknown')

embarked_port = list(df['Embarked'].unique())
gender = list(df['Sex'].unique())

col1, col2 = st. columns([1, 1])
selected_port = col1.selectbox(
    options=embarked_port,
    label='Select a Port')

selected_gender = col2.selectbox(
    options=gender,
    label='Select Gender')


