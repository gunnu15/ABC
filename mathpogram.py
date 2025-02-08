import random
num1 = 1
num2 = 10
max_attempts = 7
secret_number = random.randint(num1, num2)
def get_guess():
    while True:
        guess = int(input("Guess a number between 1 to 10:"))
        if num1 <= guess <= num2:
            return guess
        else:
            print("Invalid input, please give the number between the specified range.")
def check_guess(guess, secret_number):
    if guess == secret_number:
        return guess
    elif guess < secret_number:
        return "too low"
    else:
        return "Too high"
def play_game():
    attempts = 0
    won = False
    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)
    if result == "Correct":
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        won = True
        break
    else:
        print(f"{result}. Try again!")
    if not won:
              print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")
              if __name__ == "__main__":
                  print("Welcome to the Number Guessing Game!")
                  play_game()

