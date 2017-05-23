class Card:

    def __init__(self, data):
        self.type = data[t]
        self.questions = data[q]
        self.answers = data[a]
        self.solved = False

    def display_question(self):
        #this should only be seen while debugging. Actual cards have card types
        print(self.questions)

    def display_answer(self):
        print(self.answers)

    def receive_input(self, input):
        if input in self.answers:
            self.solved = True
            return "Correct"
        else:
            return "False"
