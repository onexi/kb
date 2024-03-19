import openai
import json

# load your key into openai
key = json.load(open('keys.env'))['OPENAI_API_KEY']
openai.api_key  = key

# call openai - chat completions
