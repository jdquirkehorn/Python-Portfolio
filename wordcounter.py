#Jay QH
#word counter
#count words in a string

#functions

def wordcounter(text):
    text2 = text.split()
    nmbr = len(text2)
    print(nmbr)
    print(f"Your text has {nmbr} words")

#main

wordcounter("Hello I am Benjamin")
