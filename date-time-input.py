import streamlit as st
from datetime import time
import time as ts

birthday = st.date_input("My birthday")

timer = st.time_input("Timer", value=time(0, 0, 0)) # set default value 0 hours, 0 minutes, 0 seconds

# timer is a datetime object
if str(timer) == "00:00:00":
    st.write("Please set the timer.")
else:
    st.write("Performing timer countdown")
    