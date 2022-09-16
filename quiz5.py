class BankAccount:
    
    def __init__(self,account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type
    
    def __repr__(self):
        return f"< Bank Account : {self.account} {self.balance} {self.owner} {self.type} >"

class Bank(BankAccount):
    def __init__(self, account_number, balance, owner, type, name, accounts):
        super().__init__(account_number, balance, owner, type)
        self.name = name
        self.accounts = accounts
        
    def __repr__(self):
        return f"< Bank Account : {self.name} {self.accounts} >" # Add an argument here
    
    
class Customer(BankAccount):
    def __init__(self,account_number, balance, owner, type,name,accounts):
        super().__init__(account_number,balance,owner,type)
        self.name = name
        self.accounts = accounts
        
    def __repr__(self):
        return f"< Customer : {self.name} {self.name}  >"

class Transactions:
    def __init__(self, account, amount, type):
        self.account = account
        self.amount = amount
        self.type = type
        
    def __repr__(self):
        return f"< Transactions : {self.account} {self.amount} {self.type} >"
    
    

