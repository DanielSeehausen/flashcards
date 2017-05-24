class Card:

    def __init__(self, data):
        self.data = data
        self.type = data['t']
        self.questions = data['q'] if type(data['q']) is list else [data['q']]
        self.answers = data['a'] if type(data['a']) is list else [data['a']]

    def display_header(self):
        print('\t*****')

    def display_footer(self):
        print('\n\n')

    def display_question(self):
        self.display_header()
        for question in self.questions:
            print('\t' + question)
        print('')

    def display_answer(self):
        for answer in self.answers:
            print('\t' + answer)
        self.display_footer()

    # we converted singular answers to a list so we can check against all options
    def check_answer(self, input):
        return True if input in self.answers else False

    def __str__(self):
        str_builder = []
        for k, v in self.data.items():
            str_builder.append(str(k) + ': ' + str(v) + '\n')
        return '\t'.join(str_builder)
