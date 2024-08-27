from chatbot import AIChatBot
from models import Provider

def main():
    message = input("Input your message: " )
    bot = AIChatBot(human_message=message, provider=Provider.OPENAI)
    print(bot.startChat())

if __name__ == "__main__":
    main()



