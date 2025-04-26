import random

while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            player_guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if player_guess < secret_number:
                print("Too low! Try again.")
            elif player_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"You guessed the number in {attempts} attempts")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Goodbye!")
        break