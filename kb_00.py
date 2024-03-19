# --------------------------------------------------------
#  pip install langchain
#  pip install -U langchain-openai
#  pip install -U langchain-community
#  pip install -U langchain-text-splitters
#  pip install faiss-cpu
#  pip install faiss-gpu
# --------------------------------------------------------
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
import json

# ----------------------------------
#  make file chunks
# ----------------------------------

# extract the text from the file
def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        return text

# read the file
text = read_file('doc/techcrunch.txt')

# # debug statements
# print(len(text))
# print(text[:100])

# lets split the text into chunks
# note, chunk size is characters, not tokens

# ----------------------------------
#  make embeddings
# ----------------------------------

# get embeddings from OpenAI

# create a vector store

# search

# debug statement
# print(docs)

# ----------------------------------
#  Basic QA Chain
# ----------------------------------

# we are going to stuff all the docs in at once

# lets ask a question
