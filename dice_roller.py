import random

def roll_dice():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    print(f"🎲 You rolled: {die_1} and {die_2} → Total: {die_1 + die_2}")

def main():
    print("🎲 Dice Roller")
    while True:
        input("Press Enter to roll the dice (or type 'q' to quit): ")
        if input == 'q':
            break
        roll_dice()

if __name__ == "__main__":
    main()
