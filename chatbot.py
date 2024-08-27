from langchain_core.messages import AIMessage
from langchain_core.messages import HumanMessage
from models import Provider, AIModel


class ChatBot():
    def __init__(self, name, message):
        self.name = name
        self.message = message
    
    def greetUser(self):
        print(f"{self.message} {self.name}")

class AIChatBot(AIModel):
    def __init__(self, human_message: str, provider: Provider):
        super.__init__(provider)
        self.human_message = human_message

    def chatStart(self):
        return self.model.invoke([HumanMessage(content=self.human_message)]).text