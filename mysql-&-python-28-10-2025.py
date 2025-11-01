#create.py
import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Students"
    )

def create_user(name,email):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO Students (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    print("Student data created successfully.")
    conn.close()

create_user("Rahul Sharma", "rahul@gmail.com")
