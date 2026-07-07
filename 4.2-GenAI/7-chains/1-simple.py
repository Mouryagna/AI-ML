from langchain_ollama import ChatOllama
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt=PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)
model=ChatOllama(model='llama3.1')
parser=StrOutputParser()

chain= prompt | model | parser

result=chain.invoke({"topic": "Black Hole"})
print(result)

## Visualize the chain

chain.get_graph().print_ascii()