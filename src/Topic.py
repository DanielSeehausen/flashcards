import importlib
from card_generator import generate_card

class Topic:

    def __init__(self, topic_name):
        try:
            card_data = importlib.import_module(topic_name).card_data
        except ImportError:
            print("%s not found in data subdirectory!" % topic_name)
            raise

        self.topic_name = topic_name
        self.solved_cards = []
        self.unsolved_cards = self.generate_all_cards(card_data)
        self.incorrect_cards = [] # (e.g. cards that the user got incorrect when answering)
        print(str(self))

    def generate_all_cards(self, card_data):
        all_cards = []
        for card in card_data:
            c = generate_card(card)
            all_cards.append(generate_card(card))
        return all_cards

    def __str__(self):
        str_builder = ['***' + self.topic_name + '***\n']
        all_cards = self.solved_cards + self.unsolved_cards + self.incorrect_cards
        for idx, card in enumerate(all_cards):
            str_builder.append(str(idx+1) + '.\t' + str(card) + '\n')
        return '\n'.join(str_builder) + '\n'
