# Import Dependencies
import nltk
from nltk.chat.util import Chat, reflections

# Run this command for first-time use
# nltk.download('punkt')

# Define the chatbot responses
pairs = [
    [
        r"hi|hello|hey|greetings",
        ["Hello! How can I assist you today?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! It's nice to meet you. How can I help?",]
    ],
    [
        r"(.*)how are you ?",
        ["I'm doing great! Thank you for asking.", "I'm here to assist you. How about you?",]
    ],
    [
        r"what is your name?",
        ["You can call me Chatbot!", "I am Chatbot, your friendly assistant."]
    ],
    [
        r"what is your age?",
        ["I am ageless! Just a program here to help you."]
    ],
    [
        r"what can you do?",
        ["I can answer your questions, provide information, and have a chat with you."]
    ],
    [
        r"do you like (.*)",
        ["I enjoy learning about %1!", "I find %1 interesting. What about you?"]
    ],
    [
        r"(.*) weather in (.*)?",
        ["I can't provide real-time weather updates, but I hope it's pleasant in %2!"]
    ],
    [
        r"(.*) (favourite|favorite) (sportsperson|player)?",
        ["I like many athletes, including Cristiano Ronaldo, Virat Kohli, and Lionel Messi!"]
    ],
    [
        r"(.*) help(.*)",
        ["I'm here to assist you! Please tell me how I can help."]
    ],
    [
        r"quit",
        ["Goodbye! Have a productive day."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that.", "Could you rephrase your question?", "Can you ask me something else?"]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Define the conversation loop
def chat():
    print("Hello! I am your friendly chatbot. Type 'quit' anytime to exit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Start the conversation
if __name__ == "__main__":
    chat()
