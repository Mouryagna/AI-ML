from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text="Delhi is the capital of India"

# result=embedding.embed_query(text)

docs=[
    "Delhi is capital of india",
    "Good Morning, How are you?",
    "Paris is the capital of France"
]
result=embedding.embed_query(text)
print(str(result))