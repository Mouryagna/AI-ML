from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOllama(model='llama3.1')

template1=PromptTemplate(
    template="Write a detailed report on the {topic}",
    input_variables=['topic']
)

template2=PromptTemplate(
    template="Write a 5 line summary on the following text.\n {topic}",
    input_variables=['topic']
)

prompt1=template1.invoke({'topic':'Black Hole'})
result=model.invoke(prompt1)

prompt2=template2.invoke({'topic':result.content})
result1=model.invoke(prompt2)

print(result1.content)