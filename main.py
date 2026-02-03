import random

def play_game():
    print("\n===== NUMBER GUESSING GAME =====")

    # Difficulty Selection
    print("Choose Difficulty Level:")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 200)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        max_range = 50
    elif choice == "2":
        max_range = 100
    else:
        max_range = 200

    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI have chosen a number between 1 and {max_range}")
    print("Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print(" Higher number please!")
        elif guess > secret_number:
            print("Lower number please!")
        else:
            print(f" Congratulations! You guessed it in {attempts} attempts.")
            return attempts


def main():
    best_score = None

    while True:
        attempts = play_game()

        # Best Score Logic
        if best_score is None or attempts < best_score:
            best_score = attempts
            print("New Best Score!")

        print(f"Best Attempts So Far: {best_score}")

        replay = input("\nDo you want to play again? (yes/no): ").lower()

        if replay != "yes":
            print("Thanks for playing! ")
            break


# Start the game
main()
