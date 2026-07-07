from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='../10-Text-Splitters/data/iris.csv')

docs = loader.load()

print(len(docs))
print(docs[1])