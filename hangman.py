import random

CATEGORIES = {
    "countries": ["India", "Canada", "Brazil", "France", "Germany"],
    "fruits": ["apple", "banana", "mango", "orange", "papaya"],
    "sports": ["cricket", "football", "hockey", "tennis", "badminton"],
    "animals": ["tiger", "elephant", "giraffe", "monkey", "rabbit"],
    "colors": ["purple", "yellow", "orange", "violet", "indigo"]
}

def choose_category():
    print("Select a category:")
    for i, category in enumerate(CATEGORIES.keys(), 1):
        print(f"{i}. {category.capitalize()}")
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice in [str(i) for i in range(1, 6)]:
            return list(CATEGORIES.keys())[int(choice) - 1]
        else:
            print("Invalid input. Please enter a number from 1 to 5.")

def choose_word(category):
    return random.choice(CATEGORIES[category])

def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_valid_input(already_guessed):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter.")
        else:
            return guess

def play_hangman():
    category = choose_category()
    word = choose_word(category)
    guessed_letters = []
    attempts_left = 6

    print(f"\nCategory selected: {category.capitalize()}")
    print("Guess the word, one letter at a time.")
    print(f"You have {attempts_left} incorrect attempts.\n")

    while attempts_left > 0:
        print(display_current_state(word, guessed_letters))
        guess = get_valid_input(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!\n")
        else:
            attempts_left -= 1
            print(f"Wrong guess. Attempts left: {attempts_left}\n")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return

    print(f"Game Over! The word was: {word}")

def main():
    while True:
        play_hangman()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing Hangman. Goodbye!")
            break

if __name__ == "__main__":
    main()
