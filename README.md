This is a chatbot the responds to questions relating to JPMorgan and its subsidiaries Nutmeg & Chase, tell a joke and perform basic arithmitic.
The chatbot comes from the ChatterBot python library. See docs here: https://docs.chatterbot.us/
The ChatterBot is trained on txt files and a csv files. When training on the files, it expects a query followed by a response - these are seperated by a new line
For example:
"Who are you?"
"I am a JPMorgan ChatBot"

The csv file's columns are seperated as so: persona, text, conversation. This helps the chatbot know who is saying each line and if it belongs to a particular conversation

The program uses Flask to listen for requests from the frontend, it uses port 5001 and url "/query" (so in all "http://localhost:5001/query")

To run it, create a virtual environment of your choosing and run "pip install -r requirements.txt" to install dependencies and run chat.py to start the chatbot

The chatbot will answer questions to the best of its abilities, but if it ever runs into a query that it cannot understand, it will respond with a default message that details the queries it can respond to
