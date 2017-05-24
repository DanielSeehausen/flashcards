from Card import Card
from string import ascii_lowercase
import random

class MultipleChoice(Card):

    def __init__(self, data):
        Card.__init__(self, data)
        self.all_choices = data['m'][:] + self.answers # no extends() available here
        random.shuffle(self.all_choices)

        self.choice_dict = {}
        for idx, choice in enumerate(self.all_choices):
            self.choice_dict[ascii_lowercase[idx]] = choice

    def display_question(self):
        Card.display_question(self)
        for ch, choice in self.choice_dict.items():
            print('\t' + ch + '. ' + choice)

    def check_answer(self, input):
        return True if self.choice_dict[input] in self.answers else False
