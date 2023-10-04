# https://www.youtube.com/watch?v=oTbbfuH44Gg&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=11

import streamlit as st
from datetime import time
import time as ts

def converter(val):
    m, s, ms = val.split(':')
    return int(m) * 60 + int(s) + (int(ms)/1000)

timer = st.time_input("Timer", value=time(0, 0, 0)) # set default value 0 hours, 0 minutes, 0 seconds

# timer is a datetime object
if str(timer) == "00:00:00":
    st.write("Please set the timer.")
else:
    bar = st.progress(0) # creates a progress bar
    num_seconds = converter(str(timer))
    per = num_seconds / 100
    for i in range(100):
        bar.progress(i+1)
        ts.sleep(per)
