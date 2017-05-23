import sys
sys.path.insert(0, './cards')
import FreeAnswer
import MultipleChoice
import PatternMatch


dispatch = {
    'f': FreeAnswer,
    'm': MultipleChoice,
    'p': PatternMatch
}

def generate_card(card_data):
    return
    # return dispatch[card_data[t]](card_data)
