from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
import json
import os;

# load the persisted database from disk
key = json.load(open('keys.env'))['OPENAI_API_KEY']
persist_directory = 'db'


# llm instance

# create the chain to answer questions 

# Cite sources

# full example
