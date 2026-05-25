from expenses import (
    add_expense,
    view_expenses,
    remove_expense,
    total
)

print("=" * 50)
print("               EXPENSE TRACKER")
print("=" * 50)

def flow():

    while True:

        print("\n Press 1 to add expense")
        print(" Press 2 to view expense")
        print(" Press 3 to remove expense")
        print(" Press 4 to view total amount of expenses")
        print(" Press 5 to exit")

        answer = input("\n")

        if answer == "1":
            add_expense()

        elif answer == "2":
            view_expenses()

        elif answer == "3":
            remove_expense()
            
        elif answer == "4":
            total()

        elif answer == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid Input")

flow()




    


