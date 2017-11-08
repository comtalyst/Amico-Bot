from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

def train(chatbot):
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    chatbot.train("chatterbot.corpus.english");

chatbot = ChatBot("Test")
train(chatbot)
print ("\nReady!")
while(True):
  raw = input('> ')
  response = chatbot.get_response(raw)
  print (response)
