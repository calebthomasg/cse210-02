import random

class Word:

    def __init__(self):
        
        self.value = ""

    def choose_word(self):

        words = ["clown", "lunch", "towel", "faith", "scowl", "cloth", "video", "piano", "horse", "stone"]
        self.value = random.choice(words)