#!/usr/bin/env python
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../data"))
sys.path.append(os.path.join(os.path.dirname(__file__), "/cards"))
from Session import Session

def main(topics=["seed_dasta"]):
    print("loading cards from the following topics: ")
    for topic in topics:
        print(topic)

    session = Session(topics)

main()
