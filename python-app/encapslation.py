class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # ❌ Error (private)
