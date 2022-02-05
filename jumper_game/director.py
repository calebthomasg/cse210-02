from jumper_game.word import Word

class Director:

    def __init__(self):

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

        for i in range(8):
            self._letter = input("Guess a letter [a-z]: ")

    def _do_updates(self):
        
        if self._letter in self._word:
            self.score = 1
        else:
            self.score = 0

    def _do_outputs(self):

        if self.score == 1:
            """Do nothing to the parachute"""
        else:
            """Remove a piece of the parachute"""
    
    