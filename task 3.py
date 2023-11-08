import random

def roll_dice(num_dice=2):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

while True:
    num_dice = int(input("Enter the number of dice to roll: "))
    results = roll_dice(num_dice)
    print("Dice roll result(s):", results)
    
    roll_again = input("Roll again? (yes/no): ").lower()
    if roll_again != "yes":
        print("Goodbye!")
        break
