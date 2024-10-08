from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Main loop to handle user input and generate responses
while True:
    # Get user input
    user_input = input('You: ')
    
    # Get chatbot response
    response = chatbot.get_response(user_input)
    
    # Print chatbot response
    print('Bot:', response)
