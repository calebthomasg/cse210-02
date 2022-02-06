import random

class Word:

    def __init__(self):
        
        self.value = ""

    def choose_word(self):
        # This is a list of five letter words.
        # The self.value variable will randomly be assigned a word from the list.
        # We'll also need to somehow divide this word into individual letters.
        # The split() function could do this.

        words = ["clown", "lunch", "towel", "faith", "scowl", "cloth", "video", "piano", "horse", "stone"]
        self.value = random.choice(words)
        