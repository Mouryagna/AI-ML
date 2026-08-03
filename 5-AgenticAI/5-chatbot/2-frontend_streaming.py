import streamlit as st
from langchain_core.messages import HumanMessage
from backend import chatbot


CONFIG={"configurable":{"thread_id":"thread_1"}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

#session_state: dict which stores messages unlike traditional dict
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input=st.chat_input("Type Here")
if user_input:

    st.session_state['message_history'].append({"role":"user","content":user_input})

    with st.chat_message("user"):
        st.text(user_input)

    # st.session_state['message_history'].append({"role":"assistant","content":ai_message})
    with st.chat_message("assistant"):

        ai_message=st.write_stream(
            message_chunk.content for message_chunk,metatdat in chatbot.stream(
                input={"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )
        st.session_state['message_history'].append({"role":"assistant","content":ai_message})