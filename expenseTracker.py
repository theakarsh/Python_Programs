# Expense Tracker

expenses = [] # list of expsenses in form of dictionaries
print("\nWelcome to Expense Tracker.")
while True:
    print("\n====MENU====")
    print("1. Add your Expenses")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    choice = int(input("Enter your choice from 1 to 4 : "))

    # 1.Add Expense
    if choice == 1:
        date = input("Date of Spending : ")
        category = input("Type of Expense(Food, Travel, Gadgets, Stationary, etc) : ")
        description = input("Give Description : ")
        amount = float(input("Enter the Amount : "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print()
        print("DONE BRO. Expense is added successfully.")
    
    # 2. View all Expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("No Expense Added")
        else:
            print("\n==== YOUR EXPENSES =====")
            count = 1
            for eachExpense in expenses:
                print(f"{count}--> {eachExpense["date"]}, {eachExpense["category"]}, {eachExpense["description"]},{eachExpense["amount"]}")
                count += 1
    
    # 3. Total Expenses
    elif choice == 3:
        total = 0
        for eachExpense in expenses:
            total += eachExpense["amount"]
        print(f"\nTOTAL EXPENSES : {total}")

    # EXIT
    elif choice == 4:
        print("Thank You for Tracking Your Expenses.\n")
        break

    else:
        print("Invalid Choice! Try Again.\n")