from jumper_game.word import Word

class Director:

    def __init__(self):
        # We can use the _is_playing variable to determine whether the game has ended or is still in progress.
        # The word variable will contain the secret word chosen randomly from a list.
        # We need to somehow break the word up into individual letters so that we can easily see if the user's guess is in that list. I was thinking that we could use the split() function for this.
        # The score variable could be used to determine which parts of the parachute need to be deleted.

        self._is_playing = True
        self._word = []
        self._letter = ""
        self.score = 0

    def start_game(self):

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        # There are eight possible moves the user can make before they lose.
        # This is where they'll make their guess.

        for i in range(8):
            self._letter = input("Guess a letter [a-z]: ")

    def _do_updates(self):
        # This is where we'll check to see if the user's input is in the randomly chosen secret word.
        # A score should be assigned accordingly.
        
        if self._letter in self._word:
            self.score = 1
        else:
            self.score = 0

    def _do_outputs(self):
        # This is where we'll take the score given and make changes to the parachute accordingly.
        # If the user's guess is correct, we'll also have to figure out a way to display the correct
        # letter on the board.

        if self.score == 1:
            """Do nothing to the parachute"""
        else:
            """Remove a piece of the parachute"""
    
    