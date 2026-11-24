import random


def play_game():
    lucky_number = random.randint(1, 50)
    while True:
        user_num = int(input("Guess a number between 1 and 50: "))

        if user_num == lucky_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_num < lucky_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print("The lucky number was:", lucky_number)
    print("Thanks for playing!")


play_game()
