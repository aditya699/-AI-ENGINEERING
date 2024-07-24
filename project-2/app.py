import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent

# Load environment variables from the .env file
load_dotenv()
google_api_key=os.environ["GEMINI_API_KEY"] 
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=google_api_key)

#Code to test llm
# result = llm.invoke("Write a ballad about India")
# print(result.content)

agent = create_csv_agent(
    llm,
    "test.csv",
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    allow_dangerous_code=True
)

agent.run("Which country has the higest GDP?")