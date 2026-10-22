# Part 1 - a menu-driven text interface (TUI) for a simple "piggy bank".
#
# This is a terminal program: it shows a menu, reads a choice, does something, and
# loops until the user quits. The menu loop is written for you - fill in the three
# TODO branches. Keep the exact wording shown (the tests look for it).

def main():
    balance = 0.0
    withdraw = 0.0
    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            balance = float(input("Amount: $").strip())
            print("New balance: $", balance, sep="")
            pass
        elif choice == "2":
            withdraw = float(input("Amount: $").strip())
            if withdraw > balance:
                print("Insufficient funds")
                print("Balance: $", balance, sep="")
                pass
            else:
                balance = balance - withdraw
                print("New balance: $", balance, sep="")
            pass
        elif choice == "3":
            print("$", balance, sep="")
            pass
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
