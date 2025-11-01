import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Students"
    )

def update_student(age):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Step 1: Add the new column 'address' to the 'Students' table
        #alter_query = "ALTER TABLE Students ADD address VARCHAR(200)"
        alter_query = "ALTER TABLE Students ADD age INT"
        cursor.execute(alter_query)

        # Step 2: Update the 'address' for the specific student
        # Note the correct syntax: UPDATE table SET column = %s WHERE condition
        #update_query = "UPDATE Students SET address = %s WHERE name = 'Rahul Sharma'"
        update_query = "UPDATE Students SET age = %s WHERE name = 'Rahul Sharma'"
        cursor.execute(update_query, (age,)) # The value must be passed as a tuple
        #cursor.execute(update_query, (address,)) # The value must be passed as a tuple



        conn.commit()
        print("Student data table updated successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        if conn:
            conn.rollback() # Rollback changes if an error occurred

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()
            print("MySQL connection is closed.")

update_student("21")
