def chatbot():
    print("Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello":
            print("Bot: Hi there! How can I help you?")
        elif user in ["hi", "hey"]:
            print("Bot: Hey! Nice to meet you")
        elif user == "how are you":
            print("Bot: I'm just a program, but I'm doing great! How about you?")
        elif user == "what is your name":
            print("Bot: I'm your friendly CodeAlpha Chatbot")
        elif user == "bye":
            print("Bot: Goodbye! Have a wonderful day")
            break
        elif user == "":
            print("Bot: Please say something...")
        else:
            print("Bot: Sorry, I didn’t understand that.")

chatbot()
