import streamlit as st
import pandas as pd
st.title("ABC")
name=st.text_input("Name: ")

age=st.slider("Age: ",0,100,25)
st.write(f'Your age is {age}')

options=['java','c++','c','javascript','python']
choice=st.selectbox("Your Fav course is: ",options)
st.write(f'Your choice is {choice}')

uploaded_file=st.file_uploader("choose CSV: ",type='csv')

if name:
    st.write("Hello "+name)

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)