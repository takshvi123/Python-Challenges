import random
leaderboard = {}
while True:
    name = input("What is your name? ")
    if name not in leaderboard:
        leaderboard[name] = float('inf')
    print(f"Hello {name}, I am thinking of a number between 0 and 101. Try to guess it!")
    num = random.randint(0, 101)

    if num % 2 == 0:
        print("Hint: It is an even number.")
    else:
        print("Hint: It is an odd number.")
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if num == guess:
                print("Amazing! You got it right!")
                if attempts < leaderboard[name]:
                    leaderboard[name] = attempts
                    print(f"New high score for {name}: {attempts} attempts!")
                else:
                    print(f"You guessed it in {attempts} attempts.")
                break
            elif guess > num:
                print("Try guessing a smaller number.")
            elif guess < num:
                print("Try guessing a larger number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("\nLeaderboard:")
    for player, score in sorted(leaderboard.items(), key=lambda x: x[1]):
        if score != float('inf'):
            print(f"{player}: {score} attempts")
    choice = input("Do you want to continue? (Yes/No): ").lower()
    if choice in ["no", "n"]:
        print("\nFinal Leaderboard:")
        for player, score in sorted(leaderboard.items(), key=lambda x: x[1]):
            if score != float('inf'):
                print(f"{player}: {score} attempts")
        break
    elif choice in ["yes", "y"]:
        continue
    else:
        print("Invalid input. Exiting the game.")
        break