def chatbot_response(user_input):
    responses = {
        "hello": "Hi! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is ai": "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.",
        "bye": "Goodbye! Have a great day!"
    }
    
    # Convert input to lowercase for matching
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

# User interaction
while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        print("Bot: Goodbye!")
        break
    print(f"Bot: {chatbot_response(user_text)}")
