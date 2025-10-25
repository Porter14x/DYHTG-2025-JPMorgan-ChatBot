"""
Chat.py is responsible for handling Chatbot conversation
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)

exit_conditions = (":q")

trainer.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

trainer.train([
    "What is your name?",
    "My name is Chatty!"
])

while True:

    query = input("> ")

    if query in exit_conditions:
        break
    else:
        print(f"Chatty: {chatbot.get_response(query)}")
