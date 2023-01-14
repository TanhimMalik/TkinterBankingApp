import tkinter as tk
from tkinter import ttk

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been added to your account. Your current balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance. Your current balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from your account. Your current balance is {self.balance}")

    def view_balance(self):
        print(f"Your current balance is {self.balance}")

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank Application")
        self.geometry("600x400")
        self.configure(bg='#2c3e50')
        self.user = Bank(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your gender: "))

        self.name_label = tk.Label(self, text=f"Name: {self.user.name}", font=("Helvetica", 16), bg='#2c3e50',
                                   fg='white')
        self.name_label.pack()

        self.age_label = tk.Label(self, text=f"Age: {self.user.age}", font=("Helvetica", 16), bg='#2c3e50', fg='white')
        self.age_label.pack()

        self.gender_label = tk.Label(self, text=f"Gender: {self.user.gender}", font=("Helvetica", 16), bg='#2c3e50',
                                     fg='white')
        self.gender_label.pack()

        self.screen = tk.Text(self, height=2, width=30, font=("Helvetica", 18), bg='white', fg='black')
        self.screen.pack()

        self.keypad_frame = ttk.Frame(self)
        self.keypad_frame.pack(pady=10)

        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(pady=10)

        # create a list of buttons for the keypad
        self.keypad_buttons = []
        for i in range(10):
            button = tk.Button(self.keypad_frame, text=str(i), font=("Helvetica", 18), width=5, height=2,
                               command=lambda x=i: self.press(x))
            self.keypad_buttons.append(button)

        self.deposit_button = tk.Button(self.button_frame, text="Deposit", font=("Helvetica", 14), bg='#2980b9',
                                        fg='white', command=self.deposit)
        self.withdraw_button = tk.Button(self.button_frame, text="Withdraw", font=("Helvetica", 14), bg='#2980b9',
                                         fg='white', command=self.withdraw)
        self.balance_button = tk.Button(self.button_frame, text="View Balance", font=("Helvetica", 14), bg='#2980b9',
                                        fg='white', command=self.user.view_balance)

        # Add the keypad buttons to the keypad frame in a grid
        for i, button in enumerate(self.keypad_buttons):
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

        self.deposit_button.pack(side=tk.LEFT)
        self.withdraw_button.pack(side=tk.LEFT)
        self.balance_button.pack(side=tk.LEFT)

    def press(self, number):
        self.screen.insert("end", str(number))

    def deposit(self):
        amount = float(self.screen.get("1.0", "end"))
        self.user.deposit(amount)
        self.screen.delete("1.0", "end")

    def withdraw(self):
        amount = float(self.screen.get("1.0", "end"))
        self.user.withdraw(amount)
        self.screen.delete("1.0", "end")

if __name__ == '__main__':
        app = BankApp()
        app.mainloop()
