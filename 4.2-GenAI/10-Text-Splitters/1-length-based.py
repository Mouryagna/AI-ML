from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("data/a.pdf")
docs=loader.load()

splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separator=""
)

result=splitter.split_documents(docs)

print(result[25].page_content)