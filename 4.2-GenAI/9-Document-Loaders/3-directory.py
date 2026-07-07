from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()

loader=DirectoryLoader(
    path="../10-Text-Splitters/data",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs=loader.lazy_load()

print(doc.metadata for doc in docs)
