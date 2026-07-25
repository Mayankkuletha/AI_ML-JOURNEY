import random
import words


hangman_art = {
    6: (
        "   --------",
        "   |      |",
        "   |      O",
        "   |     /|\\",
        "   |     / \\",
        "   |",
        "--------"
    ),

    5: (
        "   --------",
        "   |      |",
        "   |      O",
        "   |     /|\\",
        "   |     /",
        "   |",
        "--------"
    ),

    4: (
        "   --------",
        "   |      |",
        "   |      O",
        "   |     /|\\",
        "   |",
        "   |",
        "--------"
    ),

    3: (
        "   --------",
        "   |      |",
        "   |      O",
        "   |     /|",
        "   |",
        "   |",
        "--------"
    ),

    2: (
        "   --------",
        "   |      |",
        "   |      O",
        "   |      |",
        "   |",
        "   |",
        "--------"
    ),

    1: (
        "   --------",
        "   |      |",
        "   |      O",
        "   |",
        "   |",
        "   |",
        "--------"
    ),

    0: (
        "   --------",
        "   |      |",
        "   |",
        "   |",
        "   |",
        "   |",
        "--------"
    )
}


def DisplayName(wrong_guesses):
    print("************************")
    for art in hangman_art[wrong_guesses]:
        print(art)
    print("************************")


def displayHint(hint):
    print(" ".join(hint))


def displayAnswer(answer):
    print(answer)


def main():
    print("Welcome to Hangmans Game")

    answer = random.choice(words.words)

    hint = ["_"] * len(answer)

    guessedLeter = set()

    isRunning = True

    wrong_guesses = 0

    while isRunning:

        DisplayName(wrong_guesses)

        displayHint(hint)

        guess = input("Enter the letter: ").lower()

        # validation
        if len(guess) != 1 or not guess.isalpha():
            print("Enter only one alphabet.")
            continue #Seedha loop ke starting me chala jata hai. niche nhi jayega if glt cheez krenge hum kuch isliye important hai

        # already guessed
        if guess in guessedLeter:
            print("Already guessed")
            continue #Seedha loop ke starting me chala jata hai. 

        guessedLeter.add(guess)

        # correct guess
        if guess in answer:

            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

            print("Correct Guess")

        else:
            wrong_guesses += 1
            print("Wrong Guess")

        # win case
        if "_" not in hint:
            DisplayName(wrong_guesses)
            displayHint(hint)
            print("Congratulations! You Won")
            displayAnswer(answer)
            isRunning = False

        # lose case
        elif wrong_guesses == 6:
            DisplayName(wrong_guesses)
            print("You Lose! Game Over")
            displayAnswer(answer)
            isRunning = False


if __name__ == "__main__":
    main()