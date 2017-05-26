import glob, sys
from Session import Session

#TODO separate main menu
#TODO use regex to ignore multiple spaces?

NAVIGATION = {
    1 : "Start (i.e. '1 <topic_name> <topic_name> ...')",
    2 : 'List Topics',
    3 : 'How-to',
    4 : 'Exit',
}

PROMPT = '> '

def get_all_topic_names():
    return [x.split('/')[-1][:-3:] for x in glob.iglob('./data/*.py')]

def show_topics(_):
    print('\nAvailable topics (when providing topics as optional arguments for <1>, use exact names)')
    for idx, topic in enumerate(get_all_topic_names()):
        print(str(idx+1) + ' - ' + topic)
    main_menu()

def start(topics=[]):
    # by default all topics are fetched (this parses the data directory)
    if topics:
        topics = topics.split(' ')
    else:
        print("\nNo user specified topics found!")
        topics = get_all_topic_names()
    session = Session(topics)
    session.execute_session_loop()

def how_to(_):
    print('\nStart game <1> to begin testing with flash cards from all topics available OR with optional topic names, (separated by single spaces), to test only the cards within those topics (i.e. <1 topic_a topic_b>).')
    print('If you get a card incorrect, it will be presented again with all other incorrect cards once the deck has been run through once. This will repeat until you have submitted correct answers for all the cards.')
    main_menu()

def exit(_):
    print("\n\n*** Goodbye ***\n\n")
    sys.exit()

DISPATCH = {
    1 : start,
    2 : show_topics,
    3 : how_to,
    4 : exit
}

def input_valid(valid_input, user_choice):
    return True if user_choice in valid_input else False

def print_main_menu():
    print('')
    for k, v in NAVIGATION.items():
        print(str(k) + ': ' + v)
    print('')

def main_menu():
    print_main_menu()
    user_choice = input(PROMPT)
    try:
        if int(user_choice[0]) in NAVIGATION.keys():
            DISPATCH[int(user_choice[0])](user_choice[2:])
        else:
            print("\nSelect from options provided\n")
            return main_menu()
    except (ValueError, IndexError):
        print("\nInvalid input - first value must be an integer\n")
        return main_menu()
