from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

def trainCorpus(chatbot):
    chatbot.set_trainer(ChatterBotCorpusTrainer)
    #chatbot.train("./corpus/chatterbot_corpus/english/");
    chatbot.train("./corpus/test/test.yml");

def trainList(chatbot,listTrainingData):
    chatbot.set_trainer(ListTrainer)
    chatbot.train(listTrainingData);

def trainBig(chatbot):
    chatbot.set_trainer(UbuntuCorpusTrainer)
    chatbot.train();

listTrainingData = [
    u"comtalyst",
    u"Hello, Master!"
]
chatbot = ChatBot(
    "Test",
    #read_only=True,
)
#trainBig(chatbot)
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
