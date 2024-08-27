from langchain_google_vertexai import ChatVertexAI
from langchain_openai import OpenAI
from langchain_core.messages import AIMessage
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import getpass
from enum import Enum
from constants import PROVIDER_TYPE_ERROR

load_dotenv()

# OPEN_AI_KEY= os.getenv("OPENAI_KEY")
# os.environ["OPENAI_KEY"] = getpass.getpass()
PINECONE_KEY = os.getenv("PINECONE_KEY")
LANGSMITH_KEY=os.getenv("LANGSMITH_KEY")
LANGCHAIN_TRACING_V2=os.getenv("LANGCHAIN_TRACING_V2")
GOOGLE_KEY=os.getenv("GOOGLE_KEY")

class Provider(Enum):
    OPENAI = "OpenAI"
    GOOGLE = "Google"

class AIAgent(Enum):
   GEMINI = "gemini-1.5-flash"
   GPT35 = "gpt-3.5-turbo"

class AIModel():
   def __init__(self, provider:Provider):
      if not isinstance(provider, Provider):
         raise ValueError(PROVIDER_TYPE_ERROR)
      
      self._provider = provider

      if self.provider == Provider.GOOGLE:
         self.model = ChatVertexAI(model=AIAgent.GEMINI)

      elif self.provider == Provider.OPENAI:
         self.model = OpenAI(model="gpt-3.5-turbo")
      
   @property
   def provider(self):
      return self._provider
    
   @provider.setter
   def provider(self, value):
      if not isinstance(value, Provider):
         raise ValueError(PROVIDER_TYPE_ERROR)
      
      self._provider = value
   
   def invoke_model(self, message):
      return self.model.invoke([HumanMessage(content=message)]).content
    
   def __str__(self):
      return f"AIModel uses provider {self.provider.value}"


