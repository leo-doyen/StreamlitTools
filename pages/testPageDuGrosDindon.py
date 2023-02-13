import streamlit as st
import pandas as pd
from definitions.separator import get_separator
from PIL import Image
from functions.basicChackForEachColumns import basicCheck
from functions.deleteUselessColumns import drop_useless_col

st.markdown("# Gros dindon")

option = st.selectbox('Choose separator', get_separator())
st.write('Separator selected:', option)

uploaded_file = st.file_uploader("Choose a CSV file")


if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, sep=option,  encoding='Latin-1')
    
if st.button('Display the file'):
    st.dataframe(dataframe)
    # basicCheck(dataframe, dataframe.columns)


if st.button('Run basic check (higlight all columns with useless infos)'):
    basicCheck(dataframe, dataframe.columns)    

if st.button('Run mid check (delete all columns with to much disparity of values >99%)'):
        newData = drop_useless_col(dataframe)
        st.dataframe(newData)  