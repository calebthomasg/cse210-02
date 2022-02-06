def board(self):
    # This is just a basic idea of how the board will look at the very beginning of the game.
    # I'm not sure if we want this to be a class or if we should just leave it as a function and
    # add it to an existing class.

    if self._is_playing == True:
        print("_ _ _ _ _")
        print("  ___  ")
        print(" /___\ ")
        print(" \   / ")
        print("  \ /  ")
        print("   O   ")
        print("  /|\  ")
        print("  / \  ")
        print("\n^^^^^^^")