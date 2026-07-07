import os
from langchain_ollama import ChatOllama
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)
model1=ChatOpenAI()
model2=ChatHuggingFace(llm=llm)
model3=ChatOllama(model="llama3.1")

prompt1=PromptTemplate(
    template="Generate short and simple notes on following topic: \n {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Generate 5 short questions answers from the following topic:\n {topic}",
    input_variables=['topic']
)
prompt3=PromptTemplate(
    template="Merge the provided notes and quiz into a following document \n notes-> {notes} and quiz-> {quiz}",
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

chain1=prompt1 | model1 | parser
chain2=prompt2 | model2 | parser
parallel_chains=RunnableParallel({
    "notes": chain1,
    "quiz": chain2,

})
merge_chain= prompt3 | model3 | parser
chain=parallel_chains | merge_chain

result=chain.invoke({"topic": "SVM"})
print(result)