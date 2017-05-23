import sys
sys.path.insert(0, './cards')
from FreeAnswer import FreeAnswer
from MultipleChoice import MultipleChoice
from PatternMatch import PatternMatch


dispatch = {
    'f': FreeAnswer,
    'm': MultipleChoice,
    'p': PatternMatch
}

def generate_card(card_data):
    return dispatch[card_data['t']](card_data)
