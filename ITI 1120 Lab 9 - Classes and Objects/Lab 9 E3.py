class BankAccount:
    def __init__(self,name='Dupont',solde=1000):
        self.name = name
        self.solde = solde

    def deposit(self,sums=0):
        self.solde+=sums

    def withdraw(self,sums=0):
        self.solde-=sums

    def display(self):
        print("The solde of the Bank account of",self.name,"is",self.solde,"dollars.")
