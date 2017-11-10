from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

def trainCorpus(chatbot):
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    chatbot.train("chatterbot.corpus.english");

def trainList(chatbot,listTrainingData):
    chatbot.set_trainer(ListTrainer)
    chatbot.train(listTrainingData);

listTrainingData = [
    u"comtalyst",
    u"Hello, Master!"
]
chatbot = ChatBot(
    "Test",
    #read_only=True,
)
trainCorpus(chatbot)
trainList(chatbot,listTrainingData)
print("\nReady!")
while(True):
    try:
        userInput = input('> ')
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    response = chatbot.get_response(userInput)
    print(response)
