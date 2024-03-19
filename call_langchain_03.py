# -------------------------------------
# To work with strings, let's add a 
# simple output parser to convert 
# the chat message to a string.
# -------------------------------------
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
import json

# load your key into openai
key = json.load(open('keys.env'))['OPENAI_API_KEY']
llm = ChatOpenAI(openai_api_key=key)

# call openai - chat completions

# create chain

# call chain
