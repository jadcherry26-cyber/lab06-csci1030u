# Part 1 - a menu-driven text interface (TUI) for a simple "piggy bank".

def main():
    balance = 0.00
    withdraw = 0.00
    while True:
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Balance")
        print("4) Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            balance = float(input("Amount: $").strip())
            print("New balance: ${:.2f}".format(balance), sep="")
            pass
        elif choice == "2":
            withdraw = float(input("Amount: $").strip())
            if withdraw > balance:
                print("Insufficient funds")
                print("Balance: ${:.2f}".format(balance), sep="")
            else:
                balance = balance - withdraw
                print("New balance: ${:.2f}".format(balance), sep="")
            pass
        elif choice == "3":
            print("Current balance: ${:.2f}".format(balance), sep="")
            pass
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
