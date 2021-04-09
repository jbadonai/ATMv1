import random
from datetime import date
import os

database = {0:{'fName':'joe', 'lName':'james','email':'joe@james.com', 'password':'123','balance':100}}
currentUser = ""
currentAccountNo = 0


def cls():
    os.system("cls")


def get_current_date():
    return date.today().strftime("%B %d, %Y")


def register_header():
    cls()
    print('Welcome to BankPython Registration Page'.center(50))
    print(("*" * 40).center(50))
    print(get_current_date().rjust(50))
    print()
    print("REGISTER".ljust(50))
    print()


def account_activity_header(username):
    cls()
    # print(f"username here: {username}")
    print('Welcome to BankPython Activity Page'.center(50))
    print(("*" * 40).center(50))
    print(get_current_date().rjust(50))
    print()
    print("%s, Please see the available options below: " % username)
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Account Balance")
    print("4. Complaints")
    print("5. Logout")
    print()


def main_header():
    cls()
    print('Welcome to BankPython'.center(50))
    print(("*" * 40).center(50))
    print(get_current_date().rjust(50))
    print()
    print("What would you like to do? ".ljust(50))
    print()

    print("1. Login")
    print("2. Register")


def login_header():
    cls()
    print('Welcome to BankPython Login Page'.center(50))
    print(("*" * 40).center(50))
    print(get_current_date().rjust(50))
    print()

    print()


def register():
    global currentAccountNo
    global currentUser

    register_header()
    fName = input("Please enter your First Name: \n")
    lName = input("Please enter your Last Name: \n")
    email = input("Please enter your email Address Name: \n")
    password = input("Please create a password: \n")
    accountNo = int(generate_account_no())
    database[accountNo] = {'fName': fName, 'lName': lName, 'email': email, 'password': password, 'balance': 100}

    print()
    print("Congratulations! Your new account has been created. See the details below:")
    print(f"Account No. {accountNo}")
    print(f"First Name. {fName}")
    print(f"Last name:  {lName}")
    print(f"Password:  {password}")

    input("press enter to goto Login page.")
    main_page()


def login():
    global currentAccountNo
    global currentUser
    try:
        login_header()
        accountNo = int(input("Please enter your Account Number: \n"))
        if accountNo in database:
            attempt = 0
            while True:
                attempt += 1
                password = input("Please enter your password:")
                if database[accountNo]['password'] == password:
                    print("Login successful")

                    currentUser = database[accountNo]['fName']
                    currentAccountNo = accountNo

                    account_activity()
                    break
                else:
                    print(f"Wrong Password Please Try again: Failed attempts: {attempt}")
                    if attempt == 3:
                        main_page()
                        break
        else:
            print("Account number does not exist. Please register An account First")
            ans = input("Will you like to register an account now?[enter 'y' for Yes and 'n' for No:] \n")
            if ans == 'y' or ans == 'Y':
                register()
            else:
                main_page()
    except Exception as e:
        print(f"Error!: {e}")


def generate_account_no():
    return random.randrange(1111111111, 9999999999)


def withdrawal():
    try:
        cls()
        print('Welcome to BankPython Withdrawal Page'.center(50))
        print(("*" * 40).center(50))
        print(get_current_date().rjust(50))
        print()

        amount = input("Please specify amount to be withdraw or 'e' to go back to main menu: \n")
        if str(amount) == 'e' or str(amount) == 'E':
            account_activity()

        amount = int(amount)
        balance = database[currentAccountNo]['balance']

        if amount < balance:
            print(f"Withdrawal of N{amount} was successful\n")
            print(f"Your current balance is {balance - amount}")
            # update account balance
            database[currentAccountNo]['balance'] = balance - amount

            print()
            input('Press Enter to return to main page:')
            account_activity()
        else:
            print("You do not have sufficient amount in your account.")

            print()
            input('Press Enter to try again:')
            withdrawal()

    except Exception as e:
        print(e)
        account_activity()


def check_balance():
    global currentAccountNo
    global currentUser
    try:
        cls()
        print('Welcome to BankPython Account Balance Page'.center(50))
        print(("*" * 40).center(50))
        print(get_current_date().rjust(50))
        print()

        print(f"Your account balance is: {database[currentAccountNo]['balance']}")
        print()
        input('Press Enter to return to main page:')
        account_activity()
    except:
        account_activity()


def deposit():
    global currentAccountNo
    global currentUser
    try:
        cls()
        print('Welcome to BankPython Deposit Page'.center(50))
        print(("*" * 40).center(50))
        print(get_current_date().rjust(50))
        print()

        amount = int(input("Please specify amount to deposit: "))
        curr_bal = database[currentAccountNo]['balance']
        new_balance = amount + curr_bal

        database[currentAccountNo]['balance'] = new_balance

        print(f"Account deposit successfull")
        print(f"Current balance is:{new_balance}")

        input('Press Enter to return to main page:')
        account_activity()
    except:
        account_activity()


def complaints():
    global currentAccountNo
    global currentUser
    try:
        cls()
        print('Welcome to BankPython Complaints Page'.center(50))
        print(("*" * 40).center(50))
        print(get_current_date().rjust(50))
        print()

        ans = input("What issue will you like to report: \n")

        print()
        print("Complaint:")
        print(ans)
        print()

        print(f"Your Issue above has been noted and forwarded to right channel for resolution. \n"
              f"We will contact you soon on your registered email address - {database[currentAccountNo]['email']}")

        print()
        input('Press Enter to return to main page:')
        account_activity()
    except:
        account_activity()


def account_activity():
    global currentAccountNo
    global currentUser
    try:
        currentUser = database[currentAccountNo]['fName']

        account_activity_header(currentUser)
        ans = int(input("Please select an option:"))
        if ans == 1:
            withdrawal()
        if ans == 2:
            deposit()
        if ans == 3:
            check_balance()
        if ans == 4:
            complaints()
        if ans == 5:
            main_page()
        else:
            print("Error! Wrong input supplied. Try again.")
            account_activity()
    except:
        account_activity()


def main_page():
    global currentAccountNo
    global currentUser
    try:
        main_header()
        currentAccountNo = None
        currentUser = None
        ans = int(input("Please select and option:\n"))
        if ans == 1:
            login()
        if ans == 2:
            register()
        else:
            main_page()
    except:
        main_page()


main_page()

