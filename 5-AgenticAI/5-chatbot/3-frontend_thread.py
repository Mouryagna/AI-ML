import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage
from backend import chatbot
import uuid

# utility function

def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conv(thread_id):
    state=chatbot.get_state(config={"configurable":{"thread_id":thread_id}})

    return state.values.get('messages',[])


# session setup
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

if "thread_id" not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state['chat_threads']=[]

add_thread(st.session_state['thread_id'])


# Side bar

st.sidebar.title("CHAT BOT")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My conversations")

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']=thread_id
        messages=load_conv(thread_id)

        temp_messages=[]
        for message in messages:
            if isinstance(message,HumanMessage):
                role="user"
            else:
                role="assistant"
            temp_messages.append({"role":role, "content":message.content})

        st.session_state['message_history']=temp_messages


# main UI

#loading conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input=st.chat_input("Type Here")

if user_input:

    st.session_state['message_history'].append({"role":"user","content":user_input})

    with st.chat_message("user"):
        st.text(user_input)

    CONFIG = {"configurable": {"thread_id": st.session_state['thread_id']}}

    with st.chat_message("assistant"):
        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            ):
                if isinstance(message_chunk, AIMessage):
                    # yield only assistant tokens
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})