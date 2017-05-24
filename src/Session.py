from Topic import Topic

class Session:

    def __init__(self, topics):
        self.get_topics(topics)
        self.complete = False
        self.round = 0

    def get_topics(self, topics):
        self.topics = dict.fromkeys(topics)
        print("\nLoading cards from the following topics: ")
        for topic in topics:
            try:
                self.topics[topic] = Topic(topic)
                print('\t' + u'\u2713 ' + topic + '...loaded')
            except ImportError:
                print('\t' + u'\u2718 ' + topic + '...not found!')
