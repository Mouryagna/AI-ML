from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Summarize the following text\n {text}",
    input_variables=['text']
)
parser=StrOutputParser()
model=ChatOllama(model="llama3.1")

report_chain=prompt1 |model |parser

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=report_chain | branch_chain
print(final_chain.invoke({"Topic": "AI"}))