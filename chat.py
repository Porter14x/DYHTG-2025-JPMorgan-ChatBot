"""
Chat.py is responsible for handling Chatbot conversation
"""

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, CsvFileTrainer

import sanitiser as s

chatbot = ChatBot('Chatty',
                  logic_adapters=[             
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I Am sorry, but I do not understand. I can answer questions about JPMorgans history,\n provided services, such as Asset & Wealth Management, Commercial & Investment Banking, and work on Technology\n and career oppurtunities',
            'maximum_similarity_threshold': 0.95
        }
    ])

trainer = ListTrainer(chatbot)
trainercsv = CsvFileTrainer(
    chatbot,
    field_map={
        'persona': 0,
        'text': 1,
        'conversation': 2,
    }
)

exit_conditions = (":q")

trainer.train(s.sanitise_txt("financialdata.txt"))

trainercsv.train("jpmdata.csv")

while True:

    query = input("> ")

    if query in exit_conditions:
        break
    else:
        print(f"Chatty: {chatbot.get_response(query)}")
