import random
from Topic import Topic

PROMPT = '\t--> '

def print_topic_completed(topic):
    print("\n*****\n" + topic + "COMPLETED\n*****\n")

class Session:

    def __init__(self, topics):
        self.gen_topics(topics)
        self.complete = False
        self.round = 0

    def gen_topics(self, topics):
        self.topics = dict.fromkeys(topics)
        print("\nLoading cards from the following topics: ")
        for topic in topics:
            try:
                self.topics[topic] = Topic(topic)
                print('\t' + u'\u2713 ' + topic + '...loaded')
            except ImportError:
                print('\t' + u'\u2718 ' + topic + '...not found!')

    def run_card(self, card):
        card.display_question()
        result = card.check_answer(input(PROMPT))
        if result:
            print('\n\t' + u'\u2713 '*3 + '\n')
            card.display_note()
        else:
            print('\n\t' + u'\u2718 '*3 + '\n')
        return result

    def run_random_card(self, round_topics):
        topic_name, topic = random.sample(round_topics.items(), 1)[0]
        # removes the round topic once all cards have been attempted
        if len(topic.unsolved_cards) <= 1:
            round_topics.pop(topic_name, None)
        return self.run_card(topic.get_card())

    def get_unsolved_topics(self):
        unsolved_topics = {}
        for topic_name, topic in self.topics.items():
            if not topic.is_completed():
                unsolved_topics[topic_name] = topic
        return unsolved_topics

    def end_session(self):
        self.complete = True
        print("Session complete. Total rounds: " + self.round)
        return

    def execute_session_loop(self):
        self.round += 1
        round_topics = self.get_unsolved_topics()
        if not len(round_topics):
            self.end_session()
        if self.round > 1:
            self.reset_cards(round_topics)
        print("\nStarting round " + str(self.round) + ".")
        self.start_round(round_topics)

    def prompt_user_for_round_start(self):
        input('\nEnter to begin')
        print(chr(27) + "[2J")

    def print_topics(self, round_topics):
        print("TOPICS: ", end = "")
        for topic_name in round_topics.keys():
            print(topic_name + " || ", end = "")

    def execute_round(self, round_topics):
        while round_topics:
            self.run_random_card(round_topics)
            print('\n\n') # footer to give some space between cards

    def start_round(self, round_topics):
        self.print_topics(round_topics)
        self.prompt_user_for_round_start()
        self.execute_round(round_topics)

    def reset_cards(self, round_topics):
        for topic_name, topic in round_topics.items():
            topic.prep_next_round()
