import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class BankManagementSystem:
    def __init__(self, root):  # Fixed __init__ method
        self.root = root
        self.root.title("Bank Management System")

        self.accounts = {}

        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        # Create a frame to contain all widgets
        frame = tk.Frame(self.root, bg='lightblue')
        frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Create buttons for different operations
        create_account_button = tk.Button(frame, text="Create Account", command=self.create_account, bg='lightgreen', width=20)
        create_account_button.grid(row=0, column=0, pady=10)

        deposit_button = tk.Button(frame, text="Deposit", command=self.deposit, bg='lightgreen', width=20)
        deposit_button.grid(row=1, column=0, pady=10)

        withdraw_button = tk.Button(frame, text="Withdraw", command=self.withdraw, bg='lightgreen', width=20)
        withdraw_button.grid(row=2, column=0, pady=10)

        balance_button = tk.Button(frame, text="Check Balance", command=self.check_balance, bg='lightgreen', width=20)
        balance_button.grid(row=3, column=0, pady=10)

        transfer_button = tk.Button(frame, text="Transfer Funds", command=self.transfer_funds, bg='lightgreen', width=20)
        transfer_button.grid(row=4, column=0, pady=10)

        # Create calculator widget
        calculator_label = tk.Label(frame, text="Calculator", bg='lightblue', font=('Arial', 14, 'bold'))
        calculator_label.grid(row=0, column=1, pady=10)

        calculator = tk.Frame(frame, bg='lightblue')
        calculator.grid(row=1, column=1, rowspan=3, padx=10)

        self.expression = tk.StringVar()
        entry = tk.Entry(calculator, textvariable=self.expression, font=('Arial', 12), bd=5, relief='ridge')
        entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(calculator, text=text, font=('Arial', 12), padx=10, pady=10,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # Create clock widget
        self.clock_label = tk.Label(frame, text="", bg='lightblue', font=('Arial', 14, 'bold'))
        self.clock_label.grid(row=0, column=2, pady=10)

    def create_account(self):
        account_number = simpledialog.askinteger("Create Account", "Enter account number:")
        if account_number:
            if account_number not in self.accounts:
                self.accounts[account_number] = 0
                messagebox.showinfo("Account Created", f"Account {account_number} created successfully!")
            else:
                messagebox.showerror("Error", "Account already exists!")

    def deposit(self):
        account_number = simpledialog.askinteger("Deposit", "Enter account number:")
        if account_number:
            if account_number in self.accounts:
                amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
                if amount:
                    self.accounts[account_number] += amount
                    messagebox.showinfo("Deposit", f"Deposit successful!\nCurrent balance: {self.accounts[account_number]}")
                else:
                    messagebox.showwarning("Warning", "Invalid amount!")
            else:
                messagebox.showerror("Error", "Account does not exist!")

    def withdraw(self):
        account_number = simpledialog.askinteger("Withdraw", "Enter account number:")
        if account_number:
            if account_number in self.accounts:
                amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
                if amount:
                    if self.accounts[account_number] >= amount:
                        self.accounts[account_number] -= amount
                        messagebox.showinfo("Withdraw", f"Withdrawal successful!\nCurrent balance: {self.accounts[account_number]}")
                    else:
                        messagebox.showerror("Error", "Insufficient funds!")
                else:
                    messagebox.showwarning("Warning", "Invalid amount!")
            else:
                messagebox.showerror("Error", "Account does not exist!")

    def check_balance(self):
        account_number = simpledialog.askinteger("Check Balance", "Enter account number:")
        if account_number:
            if account_number in self.accounts:
                messagebox.showinfo("Check Balance", f"Account balance: {self.accounts[account_number]}")
            else:
                messagebox.showerror("Error", "Account does not exist!")

    def transfer_funds(self):
        sender_account = simpledialog.askinteger("Transfer Funds", "Enter sender account number:")
        if sender_account:
            if sender_account in self.accounts:
                receiver_account = simpledialog.askinteger("Transfer Funds", "Enter receiver account number:")
                if receiver_account:
                    if receiver_account in self.accounts:
                        amount = simpledialog.askfloat("Transfer Funds", "Enter amount to transfer:")
                        if amount:
                            if self.accounts[sender_account] >= amount:
                                self.accounts[sender_account] -= amount
                                self.accounts[receiver_account] += amount
                                messagebox.showinfo("Transfer Funds", f"Funds transferred successfully!")
                            else:
                                messagebox.showerror("Error", "Insufficient funds!")
                        else:
                            messagebox.showwarning("Warning", "Invalid amount!")
                    else:
                        messagebox.showerror("Error", "Receiver account does not exist!")
                else:
                    messagebox.showwarning("Warning", "Receiver account number cannot be empty!")
            else:
                messagebox.showerror("Error", "Sender account does not exist!")
        else:
            messagebox.showwarning("Warning", "Sender account number cannot be empty!")

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.expression.get()))
                self.expression.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid expression: {e}")
        else:
            self.expression.set(self.expression.get() + str(text))

    def update_clock(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":  # Fixed __name__ check
    root = tk.Tk()
    app = BankManagementSystem(root)
    root.attributes('-fullscreen', True)  # Full screen
    root.mainloop()
