from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()

loader=TextLoader("../10-Text-Splitters/data/prac.txt")

text=loader.load()

model=ChatOllama(model="llama3.1")
parser=StrOutputParser()
prompt=PromptTemplate(
    template="Write a poem on {topic}",
    input_variables=['topic']
)

chain=prompt | model | parser
print(chain.invoke({"topic":text[0].page_content}))