import os
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

st.header("Research Tool")
#static
user_input=st.text_input("enter your prompt:")
if st.button("Summarize"):
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        task='text-generation',
        huggingfacehub_api_token=os.getenv("HF_TOKEN")
    )
    model=ChatHuggingFace(llm=llm)
    result=model.invoke(user_input)
    st.success(result.content)