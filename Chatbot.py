from datetime import datetime
import random

print("=== DecodeBot ===")
print("Type 'bye' to exit.\n")
user_name = ""
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Nice to meet you!"],
    "hey": ["Hey buddy!", "What's up?"],

    "how are you": [
        "I'm fine!",
        "Doing great!",
        "Awesome!"
    ],

    "what is your name": [
        "My name is DecodeBot."
    ],

    "who made you": [
        "Eng Mohamed Alaa created me."
    ],

    "thank you": [
        "You're welcome!",
        "Happy to help!"
    ],

    "good morning": [
        "Good morning!",
        "Hope you have a great day!"
    ],

    "good night": [
        "Good night!",
        "Sweet dreams!"
    ],

    "i am sad": [
        "I hope things get better soon.",
        "Stay strong!"
    ],

    "motivate me": [
        "Never stop learning.",
        "Success comes with practice.",
        "You can do it!"
    ],


    "what can you do": [
        "I can chat with you and answer simple questions."
    ],

    "are you ai": [
        "Yes! I am a simple rule-based AI chatbot."
    ],

    "bye": [
        "Goodbye!",
        "See you later!"
    ]
}

while True:
    user = input("You: ").lower().strip()

    # Save name in memory
    if "my name is" in user:
        user_name = user.replace("my name is", "").strip()
        print(f"Bot: Nice to meet you {user_name.title()}!")

    # Recall name
    elif user == "what is my name":
        if user_name:
            print(f"Bot: Your name is {user_name.title()}")
        else:
            print("Bot: I don't know your name yet.")

    # Time
    elif user == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))

    # Date
    elif user == "date":
        print("Bot:", datetime.now().strftime("%Y-%m-%d"))

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break

    # Responses from dictionary
    elif user in responses:
        print("Bot:", random.choice(responses[user]))

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand.")