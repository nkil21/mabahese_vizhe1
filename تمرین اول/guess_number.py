#سازنده ایلیا نخعی
import random

# Select a random number between 1 and 100
secret_number = random.randint(1, 100)

# Maximum number of attempts
max_attempts = 10

print("Welcome to Guess The Number Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")

# Start the game
for attempt in range(1, max_attempts + 1):

    try:
        guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess == secret_number:
            print("\nCongratulations! You WON! 🎉")
            print(f"You guessed the number in {attempt} attempts.")
            break

        # Calculate the distance from the correct number
        distance = abs(secret_number - guess)

        if guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        print(f"You are {distance} numbers away from the correct answer.")

        # Give additional hints based on distance
        if distance <= 5:
            print("Very close! 🔥")
        elif distance <= 15:
            print("Close! 😊")
        elif distance <= 30:
            print("A little far!")
        else:
            print("Far away! ❄️")

    except ValueError:
        print("Invalid input! Please enter a number.")

else:
    print("\nGame Over! You LOST! 😢")
    print(f"The correct number was: {secret_number}")
