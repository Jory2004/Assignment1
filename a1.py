import numpy as np
import pandas as pd
import streamlit as st

st.title("This is First Assignment")
st.write("This assignment is for cloud computing!!")


data = pd.DataFrame(
    {'Column1': ['A','B','C','D','E'],
     'Column2': [100,200,300,400,500]}
)

st.write("This is just a sample data.")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,4),
    columns=['A','B','C','D']
)

st.line_chart(chart_data)