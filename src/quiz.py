import glob
from Session import Session

def start(topics="all"):
    # by default all topics are fetched (this parses the data directory)
    if topics == "all":
        topics = [x.split('/')[-1][:-3:] for x in glob.iglob('./data/*.py')]

    print("loading cards from the following topics: ")
    for topic in topics:
        print(topic)

    session = Session(topics)
