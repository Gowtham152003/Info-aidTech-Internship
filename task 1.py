import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! I'm thinking of a number between 1 and 100. You have 10 attempts to guess it.")
    print("Here are the rules:")
    print("1. You need to guess a number between 1 and 100.")
    print("2. You have a maximum of 10 attempts to guess the correct number.")
    print("3. After each guess, I will tell you if your guess was too high or too low.")
    print("4. If you guess the number correctly, you win!")
    print("5. If you don't guess the number within 10 attempts, the game is over.")
    print("Let's get started!")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if user_guess < target_number:
            print("Your guess is too low. Try again.")
        elif user_guess > target_number:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations, {player_name}! You guessed the number ({target_number}) correctly in {attempts} attempts.")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                number_guessing_game()
            else:
                print("Thanks for playing! Goodbye!")
                break
    else:
        print(f"Game over, {player_name}. You've used all 10 attempts. The number was {target_number}.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            number_guessing_game()
        else:
            print("Thanks for playing! Goodbye!")

# Start the game
number_guessing_game()
