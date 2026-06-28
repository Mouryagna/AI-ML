import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool,initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

#set api the streamlit app
st.set_page_config(page_title="LangChain Maths Problem",page_icon="🧮")
st.title("LangChain Text to Maths Problem using google gemma")

groq_api_key=st.sidebar.text_input(label="Groq API key",type="password")

if not groq_api_key:
    st.info("Please enter your Groq API key")
    st.stop()

llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=groq_api_key)

#initialize the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the internet to find the various information on the tool"
)

#Initialize the math tool
def calculator_tool(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

calculator = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Useful for solving mathematical calculations"
)

prompt="""
Your are an agent tasked for solving mathematical Questions. Logically arrive at the solution and provide detailed solutions and display it point wise for the question below
Question: {question}
Answer:
"""
prompt_template=PromptTemplate(
    input_variables=['question'],
    template=prompt
)

##Combine all the tools into chain
chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions"
)
##initalize the agents
assistant_agent=initialize_agent(
    tools=[reasoning_tool,wikipedia_tool,calculator],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I am a math chatbot who can answer all your maths problems"}
    ]

for msg in st.session_state["messages"]:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

# let start interaction
question=st.text_area("Enter your question")
if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)

            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
            st.session_state.messages.append({"role":"assistant","content":response})
            st.write("Response")
            st.success(response)
    else:
        st.warning("Please enter a valid question")
