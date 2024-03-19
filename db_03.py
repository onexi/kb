# --------------------------------------------------------------------
#  pip install --quiet langchain 
#       langchain-community langchain-openai
#  pip install --quiet cohere
# --------------------------------------------------------------------

# Import necessary libraries
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter
import json

# Step 2: Setup your SQLite database connection

# step 3: Create a chain
