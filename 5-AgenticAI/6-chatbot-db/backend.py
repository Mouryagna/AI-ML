from langgraph.graph import START,StateGraph,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from dotenv import load_dotenv

load_dotenv()

model=ChatOllama(model="llama3.1:latest")
class ChatState(TypedDict):

    messages:Annotated[list[BaseMessage],add_messages] #Base - any messages AI,HUMAN,System

def chat_node(state: ChatState):

    messages=state['messages']
    response=model.invoke(messages)

    return {"messages":[response]}

conn=sqlite3.connect(database="chatbot.db",check_same_thread=False)

checkpointer=SqliteSaver(conn=conn)
graph=StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads=set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)