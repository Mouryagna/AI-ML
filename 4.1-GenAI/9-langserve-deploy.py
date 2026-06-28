from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn


import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model=ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)
system_template="Translate the following into {language}"
prompt_template=ChatPromptTemplate.from_messages([
    ("system",system_template),
    ('user',"{text}")
])
parser=StrOutputParser()
chain=prompt_template|model|parser
app=FastAPI(title="Language Chain Server",version="1.0",description="Language Chain Server")

add_routes(app,chain,path="/chain")

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
