import importlib
from card_generator import generate_card

class Topic:

    def __init__(self, topic_name):
        try:
            card_data = importlib.import_module(topic_name).card_data
        except ImportError:
            print("%s not found in data subdirectory!" % topic_name)
            raise

        self.solved_cards = []
        self.unsolved_cards = []
        self.populate_cards(card_data)

    def populate_cards(self, card_data):
        for card in card_data:
            self.unsolved_cards.append(generate_card(card))
