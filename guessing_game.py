from random import randint 

#NUMBER GUESSING GAME

def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    print("------------------------------------")
    print("Think number between 1 - 100.")
    print("You have only 10 choice\n")

    secret_number = randint(1, 100)
    attempt_limit = 10
    attempt = 0

    while attempt < attempt_limit:
        try:
            guess = int(input("Enter your number: "))

            if guess == secret_number:
                print(f"---------------------------")
                print(f"\nCongaturation, You Win!")
                print(f"You choose: {guess}.\nThe Secret number is {secret_number}")
                print(f"--------------------------\n")

                return # Exit the game if guessed correctly
            
            elif guess != secret_number:
                if guess < 1 or guess > 100:
                    print("You have to choose betwee 1 and 100")
                elif guess > secret_number:
                    print("\nYour number is Too High..")
                elif guess < secret_number:
                    print("\nYour number is Too Low..")
            
            attempt += 1 # Increment the attempt count

            remain_attempts = attempt_limit - attempt
            print(f"Your remain choice is : {remain_attempts} out of 10.\n")

            
        except ValueError:
                print("\nPlease, This game is for number only.\n")

              
                

    print(f"Oops! Out of Limit😭.\nThe Secret number was {secret_number}")



if __name__ == '__main__':
    number_guessing_game()