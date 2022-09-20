import streamlit as st
import pandas as pd
from definitions.separator import get_separator

st.markdown("# CSV Formatter")

option = st.selectbox('Choose separator', get_separator())
st.write('Separator selected:', option)

uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=option,  encoding='Latin-1')
    
if st.button('Display the file'):
    st.dataframe(dataframe)