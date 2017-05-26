#!/usr/bin/env python3

import os, sys, importlib

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# TODO better way of doing this
sys.path.append(os.path.join(os.path.dirname(__file__), "./data"))
sys.path.append(os.path.join(os.path.dirname(__file__), "./src"))
sys.path.append(os.path.join(os.path.dirname(__file__), "./src/cards"))

from quiz import main_menu

INTRO_ART = "\n**************************************\n*                                    *\n*                                    *\n*                                    *\n*          Flashcards 0.0.1          *\n*                                    *\n*                                    *\n*                                    *\n**************************************\n"

print(INTRO_ART)
main_menu()
