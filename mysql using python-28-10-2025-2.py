import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", #default for xampp
        database="Students"
    )

def read_users():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT* FROM Students")
    users=cursor.fetchall()
    for user in users:
        print(user)
    #conn.commit()
    #print("Student data created successfully.")
    conn.close()

read_users()
