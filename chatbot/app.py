from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os 
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
##langsmith tracing 
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

##pront template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respnd to the user  queries")
        ("user","Question: {question}")
    ]
)

##streamlight framework
st.title("LangChain Demo With OpenAI API")
input_text = st.text_input("Enter your question here")

##openAI LLm

llm = ChatOpenAI(
    model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


if input_text:
    st,write(chain.invoke({'question': input_text}))
