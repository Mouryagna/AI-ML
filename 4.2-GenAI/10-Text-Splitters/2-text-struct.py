from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("data/a.pdf")
docs=loader.load()

text="""
These missions have not only expanded our knowledge of the universe but have also
contributed to advancements in technology here on Earth. Satellite communications, GPS, and
even certain medical imaging techniques trace their roots back to innovations driven by
space programs.
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separator=""
)
text_chunks=splitter.split_text(text)
result=splitter.split_documents(docs)

print(result[25].page_content)