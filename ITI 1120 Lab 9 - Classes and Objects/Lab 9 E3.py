#Experimenting with derived classes and inheritance
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

class AccountSaving(BankAccount):
    def __init__(self, name='Dupont',solde = 1000):
        BankAccount.__init__(self,name='Dupont',solde=1000)
        self.rate= 0.003
        self.name = name
        self.solde = solde

    def changeRate(self,value=0.003):
            self.rate = value

    def Capitalisation(self,Month):
        print("Capitalisation of", Month,"at the monthly rate of",self.rate*100,"%.")
        for i in range(Month-1):
            self.solde = self.solde*(1+self.rate)
    
