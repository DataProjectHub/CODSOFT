import nltk # type: ignore
from nltk.tokenize import word_tokenize, sent_tokenize # type: ignore

# Ensure the correct tokenizer is available
nltk.download('punkt')

def chatbot_response(user_input):
    # Tokenize using sent_tokenize first to avoid issues
    sentences = sent_tokenize(user_input)
    tokens = [word_tokenize(sentence) for sentence in sentences]  # Tokenize each sentence

    responses = {
        "hello": "Hi! How can I assist you?",
        "ai": "AI stands for Artificial Intelligence.",
        "bye": "Goodbye! Have a great day!"
    }

    # Flatten token list
    tokens = [word for sublist in tokens for word in sublist]

    for word in tokens:
        if word.lower() in responses:
            return responses[word.lower()]

    return "I'm sorry, I don't understand that."

while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        print("Bot: Goodbye!")
        break
    print(f"Bot: {chatbot_response(user_text)}")
