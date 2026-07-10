import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain_huggingface import HuggingFaceEndpoint

## Streamlit App
st.set_page_config(page_title="Summarize Text from Youtube or website")
st.title("Summarize Text from Youtube or website")
st.subheader("summarize URL")

# API Key
with st.sidebar:
    hf_api_key=st.text_input("Huggingface API KEY",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

prompt_template="""
Provide summary of the following content:
content:{text}
"""
repo_id="mistralai/Mistral-7B-Instruct-v0.3"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=150,temperature=0.7,huggingfacehub_api_token=hf_api_key)
prompt=PromptTemplate(
    template=prompt_template,
    input_variables=['text']
)

if st.button("Summarize the content from YT or URL"):

    if not hf_api_key.strip() or not generic_url.strip():
        st.error("Please provide Huggingface API KEY or URL")
    elif not validators.url(generic_url):
        st.error("Please provide URL")
    else:
        try:
            with st.spinner("waiting.. "):
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader(generic_url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"User-Agent": "Mozilla/5.0","Accept-Language": "en-US"})
                docs=loader.load()

                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)

                st.success(output_summary)
        except Exception as e:
            st.error(e)