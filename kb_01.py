# --------------------------------------------
#  pip install langchain
#  pip install langchain-openai
#  pip install -qU langchain-text-splitters
# --------------------------------------------

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ----------------------------------
#  load documents
# ----------------------------------

# Load and process the text files
# loader = TextLoader('./doc/techcrunch.txt')

#splitting the text into

# ----------------------------------
#  create database
# ----------------------------------

# persist directory stores embeddings on disk

## here we are using OpenAI embeddings but in future we will swap out to local embeddings

# persiste the db to disk
