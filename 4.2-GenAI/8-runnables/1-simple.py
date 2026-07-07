from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_core.output_parsers import StrOutputParser

model=OllamaLLM(model='llama3.1')
prompt=PromptTemplate(
    template="Tell me about this Topic:\n{topic}",
    input_variables=['topic']
)
parser=StrOutputParser()

chain=LLMChain(llm=model,prompt=prompt,output_parser=parser)

print(chain.invoke({'topic':'Inception'}))