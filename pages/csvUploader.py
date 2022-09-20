import streamlit as st
import os
import pandas as pd
from matplotlib import pyplot as plt
import time
import numpy as np


st.markdown("# CSV Uploader")


option = st.selectbox(
'Choose separator',
('/', ',', '#',';',':','\t'))
st.write('Separator selected:', option)

uploaded_file = st.file_uploader("Choose a CSV file")





if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, sep=option,  encoding='Latin-1')
    # st.write(dataframe)
    
if st.button('Say hello'):
    dataframe
else:
    st.write('Goodbye')

