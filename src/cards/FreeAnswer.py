from Card import Card

class FreeAnswer(Card):

    def __init__(self, data):
        Card.__init__(self, data)

    def check_answer(self, input):
        return True if input[0].lower() is 'y' else false
