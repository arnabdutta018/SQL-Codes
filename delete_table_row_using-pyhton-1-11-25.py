import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Students"
    )
def delete_student(name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM Students WHERE name=%s", (name,))
    conn.commit()
    print("Student data deleted successfully")
    conn.close()

delete_student("David Johnson")    
