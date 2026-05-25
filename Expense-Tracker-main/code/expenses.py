import json
import os

def expense_info():
    name = input("Enter the name of the expense: ") 
    while True:
        try:
            amount = int(input("Enter the amount of the expense: "))
            if amount <= 0:
                print("Amount cannot be zero or negative. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    category = input("Enter the category of the expense: ")
    expense = {
        "Name": name,
        "Amount": amount,
        "Category": category
    }
    return expense

def add_expense():
    while True:
        while True:
            answer = input("Do you want to add an expense? (yes/no): ")
            if answer.lower() == "yes":
                break
            elif answer.lower() == "no":
                print("No expense added.")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                
        expense = expense_info()
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                expenses = json.load(file)
            expenses.append(expense)
            with open("expenses.json", "w") as file:
                json.dump(expenses, file)
        elif not os.path.exists("expenses.json"):
            with open("expenses.json", "w") as file:
                json.dump([expense], file)
        print("Expense added successfully!")

def view_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            for expenses in expenses:
                print(f"Your Expense Name: {expenses['Name']}, Amount: {expenses['Amount']}, Category: {expenses['Category']}")
        return expenses
    else:
        print("No expenses found.")


def remove_expense():
    with open("expenses.json") as file:
        data = json.load(file)
    i = 1    
    for expense in data:
        print(f" --------- {i} {expense["Name"]}, {expense["Amount"]}, {expense["Category"]} -----------\n")
        i = i + 1    
    while True:
        try:
            rm = int(input("Enter which no of expense you want to remove:"))
            if rm > len(data):
                print("The number you entered does not correspond to any expense")
                break
            else:
                del data[rm-1]
                with open("expenses.json", "w") as file:
                    json.dump(data, file)
                break
        except ValueError:
            print("Enter positive number only")

# Code for the price of total expenses

def total():
    total_amount = 0
    with open("expenses.json", "r") as file:
            data = json.load(file)
    for n in data:
        total_amount += n['Amount']
    print(f"Total: {total_amount}")
