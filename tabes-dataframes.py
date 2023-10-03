import streamlit as st
import pandas as pd

st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹") # use \^ tab

dict = {
    "column 1": [1,2,3,4,5,6],
    "column 2": [2,4,6,8,10,12],
    "column 3": [3,6,9,12,15,18]
}
df = pd.DataFrame(dict)
st.table(df) # allows you to view tables in full screen
st.dataframe(df) # allows you sort columns