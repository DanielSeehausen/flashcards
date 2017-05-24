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
        'q' : 'Why is choux handsome?',
        'a' : 'maru',
        'n' : 'did you know: maru is too.'
    },
    {
        't' : 'm',
        'q' : 'If ken and linus had a h@cker duel, who would win?',
        'a' : 'linus',
        'm' : ['other option', 'yet another', 'one more'],
        'n' : "You don't want to be a nag, do you?"
    },
    {
        't' : 'p',
        'q' : 'The pattern "xxa" should be matched',
        'a' : ["xxa", "XXA"],
        'n' : ['a6', 'a6']
    },
]
