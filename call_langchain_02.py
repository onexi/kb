from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json

# load your key into openai
key = json.load(open('keys.env'))['OPENAI_API_KEY']
llm = ChatOpenAI(openai_api_key=key)

# call openai - chat completions

# create chain

# call chain
