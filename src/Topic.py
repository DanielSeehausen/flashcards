import importlib, random
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

    def generate_all_cards(self, card_data):
        print('*** ' + self.topic_name + ' ***\n', end='')
        all_cards = []
        for idx, card in enumerate(card_data):
            c = generate_card(card)
            all_cards.append(generate_card(card))
            print('\r' + str(idx), end='')
        return all_cards



    def __str__(self):
        str_builder = ['***' + self.topic_name + '***\n']
        all_cards = self.solved_cards + self.unsolved_cards + self.incorrect_cards
        for idx, card in enumerate(all_cards):
            str_builder.append(str(idx+1) + '.\t' + str(card) + '\n')
        return '\n'.join(str_builder) + '\n'

    def add_to_solved(self, card):
        self.solved_cards.append(card)

    def add_to_incorrect(self, card):
        self.incorrect_cards.append(card)

    def is_completed(self):
        # print('incorrect cs: ', self.incorrect_cards, 'unsolved cs: ', self.unsolved_cards)
        return True if (len(self.incorrect_cards) == 0 and len(self.unsolved_cards) == 0) else False

    def prep_next_round(self):
        self.solved_cards = []
        self.unsolved_cards = self.incorrect_cards[:]
        self.incorrect_cards = []
        random.shuffle(self.unsolved_cards)

    def get_card(self):
        return False if self.is_completed() else self.unsolved_cards.pop()
