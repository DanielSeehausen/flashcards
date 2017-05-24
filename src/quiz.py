import glob, sys
from Session import Session

#TODO separate main menu

NAVIGATION = {
    1 : "Start (i.e. '1 <topic_name> <topic_name> ...')",
    2 : 'List Topics',
    3 : 'How-to',
    4 : 'Exit',
}

PROMPT = '> '

def start(topics=[]):
    # by default all topics are fetched (this parses the data directory)
    if topics:
        topics = topics.split(' ')
    else:
        print("\nNo user specified topics found!")
        topics = [x.split('/')[-1][:-3:] for x in glob.iglob('./data/*.py')]
    print("\nLoading cards from the following topics: ")
    for topic in topics:
        print('...' + topic)
    print('')
    session = Session(topics)

def how_to():
    print("This is help menu")
    main_menu()

def exit(_):
    print("\n\n***Goodbye***\n\n")
    sys.exit()

DISPATCH = {
    1 : start,
    1 : start,
    1 : start,
    4 : exit
}

def input_valid(valid_input, user_choice):
    return True if user_choice in valid_input else False

def print_main_menu():
    for k, v in NAVIGATION.items():
        print(str(k) + ': ' + v)
    print('')

def main_menu():
    print_main_menu()
    user_choice = raw_input(PROMPT)
    try:
        if int(user_choice[0]) in NAVIGATION.keys():
            DISPATCH[int(user_choice[0])](user_choice[2:])
        else:
            print("\nSelect from options provided\n")
            return main_menu()
    except (ValueError, IndexError) as e:
        print(e)
        print("\nInvalid input - first value must be an integer\n")
        return main_menu()
