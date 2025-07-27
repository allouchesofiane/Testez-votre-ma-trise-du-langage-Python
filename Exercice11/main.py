class BankAccount:   
    """Représente un compte bancaire avec un titulaire et un solde."""
    
    def __init__(self, account_holder, balance ):
        self.account_holder = str(account_holder)
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            print("le depot doit etre positif")
            return None
        self.balance = self.balance + float(amount)
        return self.balance
    
    def withdraw(self, amount):
        if amount >= self.balance:
            print("le mantant du retrait doit etre inferieur ou égal au mantant de votre balance")
            return None
        self.balance = self.balance - float(amount)
        return self.balance

    def display_balance(self):
        print(f"le nom du propritaire est {self.account_holder} et son solde est de {self.balance} euros")

    def __str__(self):
        return f"je m'appelle {self.account_holder}et je possede {self.balance }euros"
    
bank_account = BankAccount("sofiane", 1000)
print(bank_account.deposit(1000))
print(bank_account.withdraw(500))
print(bank_account)
