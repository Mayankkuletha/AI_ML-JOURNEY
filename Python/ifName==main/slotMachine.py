import random

# Symbols available on the slot machine
symbols = ("🍒", "🍉", "🍋", "🔔", "⭐")


# Spin the slot machine
def spin_row():
    return [random.choice(symbols) for _ in range(3)]


# Display the row
def print_row(row):
    # separator string decide karti hai ki elements ko kis cheez se join karna hai.
    print(" | ".join(row)) #list ko string m convert krega.


# Calculate winnings
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20

    return 0


# Main Game
def main():

    balance = 100

    print("*************************")
    print("🎰 Welcome to Slot Machine")
    print("*************************")

    while balance > 0:

        print(f"\nCurrent Balance: ${balance}")

        bet = input("Enter your bet amount: $")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        if bet > balance:
            print("Insufficient balance.")
            continue

        balance -= bet

        row = spin_row()

        print("\nSpinning...\n")

        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout} 🎉")
        else:
            print("You lost!")

        balance += payout

        print(f"Balance = ${balance}")

        play_again = input("\nPlay again? (y/n): ").lower()

        if play_again != "y":
            break

    print("\nGame Over!")
    print(f"Final Balance: ${balance}")


if __name__ == "__main__":
    main()