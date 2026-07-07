from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

docs=[
    "Delhi is capital of india",
    "Good Morning, How are you?",
    "Paris is the capital of France"
]

result=embedding.embed_documents(docs)

print(str(result))