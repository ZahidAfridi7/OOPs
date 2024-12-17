class Atm:
    def __init__(self):
        self.pin = None  # Initialize with None to avoid confusion
        self.__balance = 0
        self.menu()
        
    # Getter method   
    def get_balance(self):
        return self.__balance
    
    # Setter method
    def set_balance(self, new_bal):
        if type(new_bal) == int:
            self.__balance = new_bal
        else:
            print("You can only set an integer balance.")
    
    def menu(self):
        user_input = input('''
        Hi! How may I help you?
        Press 1: Create PIN
        Press 2: Change PIN
        Press 3: Check Balance
        Press 4: Withdrawal
        Press 0: Exit                   
      ''')
        
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw_balance()
        elif user_input == '0':
            exit()  # Properly call exit
        else:
            print("Invalid option! Please try again.")
            self.menu()

    def create_pin(self):
        user_pin = input("Enter your PIN: ")
        self.pin = user_pin
        user_balance = int(input("Enter your balance: "))
        self.set_balance(user_balance)  # Use setter method
        print("PIN created successfully.")
        self.menu()
        
    def change_pin(self):
        old_pin = input("Enter your current PIN: ")
        if self.pin == old_pin:
            new_pin = input("Enter new PIN to change: ")
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid current PIN.")
        self.menu()
                         
    def check_balance(self):
        user_pin = input("Enter your PIN: ")
        if self.pin == user_pin:
            print(f"Your balance is: {self.get_balance()}")  # Use getter method
        else:
            print("Sorry! Invalid PIN.")
        self.menu()
            
    def withdraw_balance(self):
        user_pin = input("Enter your PIN: ")
        if self.pin == user_pin:
            amount = int(input("Enter withdrawal amount: "))  # Convert input to int
            if amount <= self.get_balance():  # Use getter method
                self.set_balance(self.get_balance() - amount)  # Use setter method
                print(f"Withdrawal successful. Remaining balance is: {self.get_balance()}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid PIN! Cannot withdraw.")
        self.menu()

# Create an instance of the ATM
a = Atm()
a.set_balance(1000)  # Setter method now works correctly
