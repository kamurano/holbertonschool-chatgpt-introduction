class Checkbook:
    """
    Class to manage a checkbook, allowing deposits, withdrawals, and checking balances.

    Methods:
    --------
    __init__():
        Initializes the checkbook with a zero balance.
    deposit(amount):
        Deposits the specified amount into the checkbook.
    withdraw(amount):
        Withdraws the specified amount from the checkbook if sufficient funds are available.
    get_balance():
        Prints the current balance of the checkbook.
    """

    def __init__(self):
        """
        Initializes the checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
        -----------
        amount : float
            The amount to be deposited.
        """
        try:
            amount = float(amount)
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook if sufficient funds are available.

        Parameters:
        -----------
        amount : float
            The amount to be withdrawn.
        """
        try:
            amount = float(amount)
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

