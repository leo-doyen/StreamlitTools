import streamlit as st

def basicCheck(df, col) :
    # col_to_delete = 0
    for col in df.columns:
        
        if(df[col].dtypes == "int64"):
            if(len(df[col].value_counts()) == 1):
                col_to_delete = col
                print(col_to_delete)   
                colCount = df.groupby(col_to_delete)[col_to_delete]\
                .count()\
                .reset_index(name='count')

                st.dataframe(colCount) 
                st.bar_chart(colCount, x=col_to_delete, y='count')
                if st.button('Delete this column'):
                    del df[col_to_delete]
                    st.success(col_to_delete +' est détruit')

            # colCount = df.groupby(colName)[colName]\
            # .count()\
            # .reset_index(name='count')

            # st.dataframe(colCount) 
            # st.bar_chart(colCount, x=colName, y='count')

            # return col.std()

