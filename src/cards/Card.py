class Card:

    def __init__(self, data):
        self.type = data['t']
        self.question = data['q']
        self.answer = data['a']
        self.solved = False

    def display_question(self):
        print(self.question)

    def display_answer(self):
        print(self.answer)

    def check_answer(self, input):
        print("This is the generic card super. Use a specific card type for answer validation")
        return True
