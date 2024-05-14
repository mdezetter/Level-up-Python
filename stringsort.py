# Challenge: Write a python function to sort the words in a string.
# Input: string of words separated by spaces
# Output: String of words sorted alphabetically
# Ignore: case of words when sorting

def sort_words(input):
    # split() breaks apart input @ spaces and lists individual words
    words = input.split()
    # append the list to add a lowercase version of the word to the front of the word. Otherwise it puts caps first.
    # banana ORANGE apple
    # bananabanana orangeORANGE appleapple
    words = [w.lower() + w for w in words]
    # next line sorts the words
    words.sort()
    # below line takes the lowercase duplicate off the beginning of the now sorted list. 
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)