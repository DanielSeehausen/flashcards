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
        for ch, choice in sorted(self.choice_dict.items()):
            print('\t' + ch + '. ' + choice)
        print('')

    def check_answer(self, user_input):
        try:
            return True if self.choice_dict[user_input[0]] in self.answers else False
        except (ValueError, IndexError, KeyError) as e:
            return self.check_answer(input("\tEnter a valid choice: \n\t--> "))
