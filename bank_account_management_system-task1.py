import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="banking_system"
    )

'''
def create_banking_system():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE banking_system (account_no INT UNIQUE, balance FLOAT, user_id VARCHAR(50) NOT NULL, password VARCHAR(200))")
    conn.commit()
    print("Bank account management system customer data table created successfully")
    conn.close()

create_banking_system()
'''
def create_bank_customer(account_no, balance, user_id, password):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO banking_system (account_no, balance, user_id, password) VALUES (%s, %s, %s, %s)", (account_no, balance, user_id, password))
    conn.commit()
    print("Customer data added successfully")
    conn.close()

create_bank_customer(1001001, 2500.75, 1, "qwerty123")
create_bank_customer(1001002, 15176.54, 2, "P@sswOrd1")
create_bank_customer(1001003, 9567.50, 3, "Abc@123")
create_bank_customer(1001004, 20763.25, 4, "Account@2025")