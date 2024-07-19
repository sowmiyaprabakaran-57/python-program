import random

def number_guessing_game():
    low = 1
    high = 100
    
    number_to_guess = random.randint(low, high)
    
    print(f"Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {low} and {high}.")
    
    attempts = 0
    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

number_guessing_game()
