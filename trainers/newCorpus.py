import logging
import os
import sys
from chatterbot.conversation import Statement, Response
from chatterbot.utils import print_progress_bar
from chatterbot import trainers

class newCorpusTrainer(trainers.Trainer):

    def __init__(self, storage, **kwargs):
        super(newCorpusTrainer, self).__init__(storage, **kwargs)
        from chatterbot.corpus import Corpus

        self.corpus = Corpus()

    def train(self, *corpus_paths):

        # Allow a list of corpora to be passed instead of arguments
        if len(corpus_paths) == 1:
            if isinstance(corpus_paths[0], list):
                corpus_paths = corpus_paths[0]

        # Train the chat bot with each statement and response pair
        for corpus_path in corpus_paths:

            corpora = self.corpus.load_corpus(corpus_path)

            corpus_files = self.corpus.list_corpus_files(corpus_path)
            for corpus_count, corpus in enumerate(corpora):
                for conversation_count, conversation in enumerate(corpus):
                    print_progress_bar(
                        str(os.path.basename(corpus_files[corpus_count])) + " Training",
                        conversation_count + 1,
                        len(corpus)
                    )

                    previous_statement_line = []
                    statement_line = []

                    for line in conversation:
                        for text in line:
                            statement = self.get_or_create(text)
                            statement.add_tags(corpus.categories)

                            statement_line.append(statement.text)

                            if previous_statement_line != []:
                                for previous_statement_text in previous_statement_line:
                                    statement.add_response(
                                        Response(previous_statement_text)
                                    )
                            self.storage.update(statement)
                            
                        previous_statement_line = statement_line
                        statement_line = []
