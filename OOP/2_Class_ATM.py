# ATM EXAMPLE
class Atm():
    def __int__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello how would u like to procces
        1. Enter 1 for craete pin
        2. Enter 2 for deposit 
        3. Enter 1 for withdraw
        4. Enter 1 for check balance
        5. Enter 5 for exit """)
        if user_input== "1":
            self.create_pin()
        elif user_input== "2":
            self.deposite()
        elif user_input == "3":
            self.withdra()
        elif user_input == "4":
            self.check()
        elif user_input == "5":
            print("bye")

    def create_pin(self):
        self.pin =input("enter pin")
        print("pin entered")
        self.menu()

    def deposite(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter ur amount "))
            self.balance = self.balance+ amount
            print("deposited")
        else:
            print("invalid pin")
    def withdra(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter ur amount "))
            if amount < self.balance:
                print("withdran")
            else:
                print("no money")
        else:
            print("invalid pin")
    def check(self):
        temp = input("enter your pin")
        if temp == self.pin:
            balance = print(self.balance)
        else:
            print("invalid pin")

if __name__ == "__main__":
    sbi =Atm()
