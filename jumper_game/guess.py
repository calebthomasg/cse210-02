from jumper_game.word import Word

# Hi guys! This isn't working as it should. I can't seem to exit the loop.
# Any ideas?

# Import the secret word and create empty variables to use later on.
word = Word()
letters_guessed = []
turns = 0
score = 0
game_over = False

# Initiation of while loop.
while game_over == False:
    # Ask the user to enter a letter that they think is part of the secret word.
    guess = str(input("Please guess a letter [a-z]: "))
    if score <= 5 or turns <= 8:
        # Checks to see if what the user guessed has already been entered.
        if guess in letters_guessed:
            turns += 1
            print("You have already guessed that letter. Please try again.")
        # Checks to see if what the user guessed is in the secret word.
        elif guess in word:
            letters_guessed.append(guess)
            score += 1
            turns += 1
            print("You guessed correctly!")
        # Initiates if user's guess is not in the secret word.
        else:
            letters_guessed.append(guess)
            turns += 1
            print("Guess again.")
    # If the user has guessed correctly five times, they've won the game. (This is because all the words are five letters long.)
    elif score == 5:
        print("Congratulations! You have won the game.")
        game_over = True
    # If the user has lost the game.
    else:
        print("Sorry, you've lost the game.")
        game_over = True