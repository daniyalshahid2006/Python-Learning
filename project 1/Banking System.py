import csv
# with open("accounts.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["AccountNumber","Username", "Password","Balance"])
#
#

def create_account ():
        try:
            with open("accounts.csv", "r") as file:
                data = csv.reader(file)
                next(data)

                rows = []

                for row in data:
                    rows.append(row)

                count = len(rows)

                if count == 0:
                    account_number = "1000"
                else:
                    last_account = rows[-1][0]
                    last_count = int(last_account)
                    last_count = last_count + 1
                    account_number = last_count

        except FileNotFoundError:
            with open("accounts.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(["AccountNumber", "Username", "Password", "Balance"])

            account_number = "1000"

        except ValueError:
            print("Invalid account number data")
            return

        name = input("Enter your name: ")
        password = input("Enter your password: ")
        balance = "0"

        with open("accounts.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([account_number, name, password, balance])

        print("Account created successfully")
def deposit(row , rows):
    try:
        dep = int(input("Enter your deposit amount: "))
        if dep > 0:
         row[3] = float(row[3])
         row[3] = row[3] + dep
         row[3] = str(row[3])
         with open("accounts.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["AccountNumber", "Username", "Password", "Balance"])
            writer.writerows(rows)
            print("deposit successful")
        else:
            print("deposit failed")
    except ValueError:
        print("invalid input")


def withdraw(row , rows):
  try:
    amount = int(input("Enter your withdraw amount: "))
    if amount > 0 :
     row[3]= float(row[3])
     if row[3] >= amount :
      row[3] = row[3] - amount
      row[3] = str(row[3])
      with open("accounts.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["AccountNumber", "Username", "Password", "Balance"])
        writer.writerows(rows)
        print("withdraw successful")
     else:
         print("insufficient balance")
    else:
        print("Invalid amount")
  except ValueError:
     print("invalid input")

def check_balance(row ):
    print("your balance is: ", row[3])
def delete_account(row,rows):
    confirmation = input("Do you want to delete the account? y/n: ").lower()
    if confirmation == "y":
       try:
        rows.remove(row)
        with open ("accounts.csv","w") as file:
         writer = csv.writer(file)
         writer.writerow(["AccountNumber", "Username", "Password", "Balance"])
         writer.writerows(rows)
         print("account deleted successfully")
       except ValueError:
           print("account does not exist")
    else:
        print("account not deleted")

def show_accounts(rows):
         print("\n All Accounts \n")
         print("=" * 30)
         for row in rows:
             print(f"AccountNumber: {row[0]}")
             print(f"Username:  {row[1]}")
             print(f"Balance:  {row[3]}")
             print("=" * 30)
def bye():
    print("GoodBye")
def user_menu(row,rows):
    print("pick your option")
    option = ""
    while option != "6":
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Delete Account")
        print("5. Show All Accounts")
        print("6. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            deposit(row,rows)
        elif option == "2":
            withdraw(row,rows)
        elif option == "3":
            check_balance(row)
        elif option == "4":
            delete_account(row,rows)
            break
        elif option == "5":
            show_accounts(rows)
        elif option == "6":
            bye()
        else:
            print("Invalid Choice")
def login():
 try:
    with open("accounts.csv", "r") as file:
        data = csv.reader(file)
        next(data)
        account_number = input("Enter your account number: ")
        password = input("Enter your password: ")
        rows = []
        found = False
        for row in data:
            rows.append(row)
        for row in rows:
            if row[0] == account_number and row[2] == password:
                found = True
                print("Login Successful")
                print("Account Number: " + row[0])
                print("Account Name: " + row[1])
                print("Account balance: " + row[3])
                user_menu(row,rows)
                break
        if not found:
         print("Login Unsuccessful")
 except FileNotFoundError:
     print("could not find file")
 except ValueError:
     print("invalid data")
choice = ""
while choice != "3":
    print("Welcome to Banking System")
    print("\n" + "=" * 30)
    print("1.Create Account")
    print("2.login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    elif choice == "2":
        login()
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")
