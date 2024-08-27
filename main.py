from chatbot import AIChatBot

def main():
    message = input("Input your message: " )
    name = input("Input your name: ")
    bot = AIChatBot(name=name, message=message)
    print(bot.startChat())

if __name__ == "__main__":
    main()



