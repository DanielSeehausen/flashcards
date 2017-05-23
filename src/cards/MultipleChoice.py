from Card import Card

class MultipleChoice(Card):

    def __init__(self, data):
        Card.__init__(self, data)

    def check_answer(self, input):
        if input in self.answers:
            self.solved = True
            return True
        else:
            return False
