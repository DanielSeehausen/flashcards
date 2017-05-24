from Topic import Topic

class Session:

    def __init__(self, topics):
        self.get_all_topics() if topics == "all" else self.get_topics(topics)
        self.complete = False
        self.round = 0

    def get_all_topics(self):
        all_topics = False # GET EVERY PATH UNDER DATA
        pass

    def get_topics(self, topics):
        self.topics = dict.fromkeys(topics)
        for topic in topics:
            try:
                self.topics[topic] = Topic(topic)
            except ImportError:
                print("\t--> Skipping unfound topic: %s" % topic)
