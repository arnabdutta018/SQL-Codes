import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Students"
        )

#Updation of sql table row values
def update_student(old_name, new_name, new_email):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE Students SET name= %s, email=%s WHERE name=%s", (new_name, new_email, old_name))
    conn.commit()
    print("Student data updated successfully")
    conn.close()

update_student("Rahul Sharma", "David Johnson", "david@example.com")
