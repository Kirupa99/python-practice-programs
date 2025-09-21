import random
import os
#number guessing game
status=True


def play_game(guess,attempt,number):
    game_status=False
    if guess < 0 or guess > 100:
        return f"Your guess should be in the range of 0 to 100, attempts:{attempt}", False
    if guess < number:
        return f"Sorry your guess is lesser than the correct number, attempts:{attempt}",game_status
    elif guess > number:
        return f"Sorry your guess is higher than the correct number, attempts:{attempt}",game_status
    elif guess == number:
        won=10-attempt
        game_status=True
        return f"Correct you got your guess right!!Congratulations you won in {won} attempts",game_status

print("Welcome to the number guessing game")

while status:
    choice = input("Type 'easy' to enter an easy level and 'hard' to enter a hard level")
    if choice.lower() == "easy":
        print("You have 10 Attempts.")
        attempt = 10
    elif choice.lower() == "hard":
        print("You have 5 Attempts.")
        attempt = 5
    else:
        print("Invalid choice! Please type 'easy' or 'hard'.")
        continue

    number = random.randint(0, 100)
    while attempt > 0:
        guess=int(input("Enter your choice"))
        attempt -= 1
        value,game_status = play_game(guess,attempt,number)
        print(value)
        if game_status:
            break
        if attempt == 0 and not game_status:
            print(f"Sorry you lost the game!! the correct number is {number}")
    loop_choice = input("Do you want to start a new game? Press 'y' to start over, 'n' to exit: ")
    print("\n"*10)
    if loop_choice.lower() != "y":
        status = False

print("Thankyou for playing!!!")






