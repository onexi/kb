# --------------------------------------------------------------------
#  pip install --quiet langchain 
#       langchain-community langchain-openai
#  pip install --quiet cohere
# --------------------------------------------------------------------

# Import necessary libraries
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
import json

# Step 2: Setup your SQLite database connection

# step 3: Create a chain
