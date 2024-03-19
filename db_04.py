# --------------------------------------------------------------------
#  pip install --quiet langchain 
#       langchain-community langchain-openai
#  pip install --quiet cohere
# --------------------------------------------------------------------

# Import necessary libraries
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
import json

# Step 2: Setup your SQLite database connection

# step 3: Create a chain

# no need to instantiate llm - it's done in cells above
