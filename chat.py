"""
Chat.py is responsible for handling Chatbot conversation
"""
from flask import Flask, request
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, CsvFileTrainer

import sanitiser as s

app = Flask(__name__)

chatbot = ChatBot('Chatty',
                  logic_adapters=[             
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I Am sorry, but I do not understand. I can answer questions about JPMorgans history,\n provided services, such as Asset & Wealth Management, Commercial & Investment Banking, and work on Technology\n and career oppurtunities',
            'maximum_similarity_threshold': 0.95
        },
        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        }
    ],
        preprocessors=
    [
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html'
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

"""while True:

    query = input("> ")

    if query in exit_conditions:
        break
    else:
        print(f"Chatty: {chatbot.get_response(query)}")"""

@app.route('/optimise', methods=["POST"])
def query():
    request_data = request.get_json()
    query = request_data['query']

    response = {response: chatbot.get_response(query)}
    return json.dumps(response)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
