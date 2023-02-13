import streamlit as st
import pandas as pd
from definitions.separator import get_separator
from definitions.header import get_header

displayUploadFile = True
displayHeader = False
displayColumnCleaner = False

dataframe = None

st.markdown("# CSV Formatter")

if displayUploadFile:
    st.write("## Upload file")
    option = st.selectbox('Choose separator', get_separator())
    st.write('Separator selected:', option)

    uploaded_file = st.file_uploader("Choose a CSV file")

    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file, sep=option, encoding='Latin-1')
 
        if st.button('Display the file'):
            st.dataframe(dataframe.head())

        if st.button('Next', key='next1'):
            displayHeader = True
            displayUploadFile = False

if displayHeader:
    st.write("## Header")

    if dataframe is not None:
        headerFormatDetected = 'normal'
        if st.checkbox('Do you have header in file?'):
            # On essaye de trouver le format des headers
            #detect automaticly the format of header else ask to user
            headerFormatDetected = 'camelCase'
        else:
            # On demande à l'utilisateur de choisir le format des headers
            print('No header detected')
        if st.checkbox('Do you want to format header?'):
            headerFormatDetected = st.selectbox('Choose format source', get_header(), index=headerFormatDetected)
            headerFormatChoose = st.selectbox('Choose format you want', get_header())
    else:
        displayHeader = False
        displayUploadFile = True

    if st.button('Next', key='next2'):
        displayColumnCleaner = True
        displayHeader = False