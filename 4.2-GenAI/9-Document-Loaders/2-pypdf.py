from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()

loader=PyPDFLoader("../10-Text-Splitters/data/a.pdf")

docs=loader.load()

model=ChatOllama(model="llama3.1")
parser=StrOutputParser()
prompt=PromptTemplate(
    template="Write a poem on {topic}",
    input_variables=['topic']
)

print(docs[0])


chain=prompt | model | parser
print(chain.invoke({"topic":docs[8].page_content}))