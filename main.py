from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.groq import Groq
import streamlit as st
import logging
import os
import openai
from urllib.parse import urlparse, parse_qs
from streamlit_option_menu import option_menu

logging.basicConfig(level=logging.INFO)

header = """
        <style> 
            *{
                background-color: #192841;
                font-family:'Times New Roman', sans-serif;
                color:#FAF0E6;
            }
            h1{
                font-family: 'Times New Roman', sans-serif;
                color: #FFFFFF; 
            }
            h2{
                font-family: 'Times New Roman', sans-serif;
                color: #FFFFFF; 
            }
        </style>
        """
st.markdown(header, unsafe_allow_html=True)
with st.container():
        col1, col2, col3 = st.columns([1,2,3])
        with col1:
            st.image('assets/logo1.png', use_column_width=True)
        with col3:
            st.title("Lawamma")
    
st.divider()

def askBot(prompt):
    Settings.llm = Groq(model="llama3-70b-8192", api_key="API_KEY")

    # Read documents from the reader
    print("Loading documents...")
    
    docs = SimpleDirectoryReader("data").load_data()
    print(f"Loaded {len(docs)} documents.")

    # Create the index
    print("Creating the index...")
    index = VectorStoreIndex.from_documents(docs)
    print("Index created.")

    # Set up the query engine
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
    # Print the response
    print("Response: ")
    print(response)
    return response

def glossaryBot(prompt):
    Settings.llm = Groq(model="llama3-70b-8192", api_key="API_KEY")

    # Read documents from the reader
    print("Loading documents...")
    
    docs1 = SimpleDirectoryReader("data").load_data()
    print(f"Loaded {len(docs1)} documents.")

    # Create the index
    print("Creating the index...")
    index1 = VectorStoreIndex.from_documents(docs1)
    print("Index created.")

    # Set up the query engine
    query_engine1 = index1.as_query_engine()
    response1 = query_engine1.query(prompt)
    # Print the response
    print("Response: ")
    print(response1)
    return response1

selected = option_menu(
    menu_title="Main Menu",
    options=["Main Page", "Ask Legal Advice", "Glossary"],
    icons=["chat", "book"],
    menu_icon="cast",
    default_index=0,
)
if selected == "Main Page":
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.header("Your Legal Business Partner")

elif selected == "Ask Legal Advice":
    st.header("Ask Legal Advice")
    userInput = st.text_input("Your question")
    if st.button("Ask") and userInput != "":
        response = askBot(userInput)
        st.write(response.response)

else:
    st.header("Glossary")
    glossaryInput = st.text_input("Enter a word you don't understand")
    if st.button("Get Definition") and glossaryInput != "":
        response = glossaryBot(glossaryInput)
        st.write(response.response)
