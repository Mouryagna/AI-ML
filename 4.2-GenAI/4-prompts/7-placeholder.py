from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

#chat template
chat_template=ChatPromptTemplate.from_messages([
    ("system","You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human","{query}")
])

#load chat history
chat_history = []

with open("chat_history.txt", "r") as f:
    for line in f:
        if line.startswith("Human:"):
            chat_history.append(HumanMessage(content=line.replace("Human:", "").strip()))
        elif line.startswith("AI:"):
            chat_history.append(AIMessage(content=line.replace("AI:", "").strip()))

# create prompt
prompt=chat_template.invoke({'chat_history': chat_history,'query':"Where is my refund"})

print(prompt)