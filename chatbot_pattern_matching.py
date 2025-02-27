import re

def chatbot_response(user_input):
    patterns = {
        r"hello|hi|hey": "Hello! How can I assist you?",
        r"how are you": "I'm good! Thanks for asking. How about you?",
        r"(what is|define) ai": "AI stands for Artificial Intelligence, enabling machines to mimic human intelligence.",
        r"bye|goodbye": "Goodbye! Have a great day!"
    }

    for pattern, response in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    return "I'm sorry, I don't understand that."

while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        print("Bot: Goodbye!")
        break
    print(f"Bot: {chatbot_response(user_text)}")
