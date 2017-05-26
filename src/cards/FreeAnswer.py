from Card import Card

class FreeAnswer(Card):

    def __init__(self, data):
        Card.__init__(self, data)

    def display_answer(self):
        for answer in self.answers:
            print('\t[A] ' + answer)

    def check_answer(self, user_input=None):
        self.display_answer()
        try:
            honesty = input('\n\tDid you get it correct? [y/n] > ')
            return True if honesty[0].lower() is 'y' else False
        except (ValueError, IndexError) as e:
            return True # they just hit enter
