# cards have four fields:
# t : type from f', 'm', 'p' (free format, multiple choice, pattern matching)
# q : the question they initially present with
# a : the correct answer <-- IF MULTIPLE CHOICE THE CORRECT CHOICE GOES HERE
# m : the other choices (if multiple choice)
# n : any info displayed AFTER the answer is submitted

# cards have this finite state flow: --> present question (q && m). receive and validate user input against (a). display info (n)

card_data = [
    {
        't' : 'f',
        'q' : 'this is seeed data q1',
        'a' : 'sda1',
        'n' : 'sdn1.'
    },
    {
        't' : 'f',
        'q' : 'this is seeed data q2',
        'a' : 'sda2',
        'n' : 'sdn2.'
    },
]
