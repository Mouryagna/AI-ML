import streamlit as st
import pandas as pd
import numpy as np

#title
st.title("Heading of the StreamLit")

#display
st.write("Simple Text")

#DF
df=pd.DataFrame({
    "First": np.random.randint(1,10,5)
})
st.write("DF sample")
st.write(df)

#chart
chart_data = pd.DataFrame(
    [[np.random.randint(3,20,10), np.random.randint(3,20,10), np.random.randint(3,20,10)]],
    columns=['a','b','c']
)

st.line_chart(chart_data)