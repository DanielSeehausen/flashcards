simple command line script for flashcard quizzing.

add new topics with a new filename in (i.e. /data/topics_name.py)

while the amount of data loaded into the system is minimal (even if all topics are loaded), this does load topics dynamically (and will only load those requested)

REQUIRES PYTHON3!
If you are writing new python, and not running old 2.x scripts, I recommend aliasing python=python3

if you would like to make it executable do:
chmod +x flashcards.py
AND
add it to your usr/ or local user /bin
OR
simply add an alias to your .profile/.bash_profile
alias flashcards='~/Development/flashcards/flashcards.py'
