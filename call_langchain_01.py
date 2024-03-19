from langchain_openai import ChatOpenAI
import json

# read openai api key
key = json.load(open('keys.env'))['OPENAI_API_KEY']

# # load your key into openai
llm = ChatOpenAI(openai_api_key=key)

# call openai - chat completions
