def get_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you": "I'm fine, thanks for asking!",
        "what's your name": "I'm ChatBot, your virtual friend.",
        "bye": "Goodbye! Have a great day.",
        "thanks": "You're welcome!",
        "help": "You can say hello, ask how I am, or say bye to end."
    }

    return responses.get(user_input, "Sorry, I didn't understand that.")

def chat():
    print("ChatBot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("ChatBot:", response)
        
        if user_input.lower().strip() == "bye":
            break

if __name__ == "__main__":
    chat()