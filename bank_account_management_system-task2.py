import mysql.connector
from datetime import datetime
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="banking_system"
    )

def check_balance(account_no):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT balance FROM banking_system WHERE account_no = %s", (account_no,))
    users=cursor.fetchone()
    for i in users:
        print(f"The balance of the respected customer is: {i}")
    conn.close()
#check_balance("1001003")

def deposit(account_no):
    try:
        amount=float(input("Enter the amount to deposit: "))
        if amount<=10:
            print("Minimum deposit amount is 10 rupees. Please enter 10 or greater: ")
            return
    except ValueError:
        print("Invalid amount. Please enter a valid amount")
        return
    conn=get_connection()
    cursor=conn.cursor()
    #cursor.execute("CREATE TABLE transactions (account_no INT, timestamp TIMESTAMP, type VARCHAR(50) NOT NULL, amount VARCHAR(200))")
    timestamp=datetime.now()
    cursor.execute("UPDATE banking_system SET balance = balance+ %s WHERE account_no= %s", (amount, account_no))
    cursor.execute("INSERT INTO transactions (account_no, timestamp, type, amount) VALUES (%s, %s, %s, %s)", (account_no, timestamp, 'Deposit', amount))
    conn.commit()

    print(f"\nSuccessfully deposited Rs.{amount:,.2f}")
    check_balance(account_no)
    conn.close()
    
def withdraw(account_no):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawl amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT balance FROM banking_system WHERE account_no = %s", (account_no,))
    current_balance = cursor.fetchone()[0]

    if amount > current_balance:
        print("\nInsufficient funds! Your balance is Rs.{current_balance:,.2f}")
        return
    
    timestamp=datetime.now()
    cursor.execute("UPDATE banking_system SET balance = balance - %s WHERE account_no = %s", (amount, account_no))
    cursor.execute("INSERT INTO transactions (account_no, timestamp, type, amount) VALUES (%s, %s, %s, %s)", (account_no, timestamp, 'Withdrawn', amount))
    conn.commit()

    print(f"\nSuccessfully withdrew Rs.{amount:,.2f}")
    check_balance(account_no)
    conn.close()

def view_history(account_no):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT timestamp, type, amount FROM transactions WHERE account_no = %s ORDER BY timestamp DESC", (account_no,))

    transactions = cursor.fetchall()

    if not transactions:
        print("\nNo Transaction history found!")
    else:
        print("\n--- Transaction History ---")
        for t in transactions:
            print(t)
        conn.close()
    

def login():
    print("---\n Log in---")
    user_id=input("Enter User ID of the customer: ")
    password=input("Enter the Password: ")
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT account_no FROM banking_system WHERE (user_id = %s AND password = %s)", (user_id, password))
    user=cursor.fetchone()
    #conn.close()

    if user:
        print(f"\nLogin successful! Welcome, {user_id}.")
        return user[0]
    else:
        print("Invalid User ID or Password.")
        return None

ac_no = login()
print(ac_no)
print(type(ac_no))
if ac_no:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Please choose an option between (1-5): ")
        
        if choice == '1':
            check_balance(ac_no)
        elif choice == '2':
            deposit(ac_no)
        elif choice == '3':
            withdraw(ac_no)
        elif choice == '4':
            view_history(ac_no)
        elif choice == '5':
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

    



        