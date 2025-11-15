import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="studentdb"
    )

def students():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE students(
        student_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(200) NOT NULL,
        gender CHAR(1),
        date_of_birth DATE,
        email VARCHAR(255),
        contact_number VARCHAR(15),
        department_id INT,
        enrollment_date DATE,
        status VARCHAR(200)
        )
        """
    )
    conn.commit()
    print("Student data table created successfully")
    conn.close()

students()

def departments():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE departments(
                   department_id INT PRIMARY KEY AUTO_INCREMENT,
                   departement_name VARCHAR(200),
                   dept_code VARCHAR(100)
                   )
                   """
    )
    conn.commit()
    print("department data table created successfully")
    conn.close()

def courses():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE courses(
                   course_id INT PRIMARY KEY AUTO_INCREMENT,
                   course_code VARCHAR(20) NOT NULL UNIQUE,
                   course_name VARCHAR(200) NOT NULL,
                   credit INT NOT NULL,
                   department_id INT REFERENCES departments(department_id)
                   )
                   """
    )
    conn.commit()
    print("Courses table created successfully")
    conn.close()

def enrollments():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE enrollments(
                    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
                    student_id INT REFERENCES students(student_id),
                    course_id INT REFERENCES courses(course_id),
                    enrollment_date DATE
                    )
                    """
    )
    conn.commit()
    print("enrollment data table created successfully")
    conn.close()

def grades():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
                   CREATE TABLE grades(
                   grade_code VARCHAR(20) PRIMARY KEY,
                   description VARCHAR(50)
                   )
                   """
    )
    conn.commit()
    print("grades table created successfully")
    conn.close()

def instructors():
     conn=get_connection()
     cursor=conn.cursor()
     cursor.execute("""CREATE TABLE instructors(
                    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
                    ins_name VARCHAR(255),
                    department_id INT REFERENCES departments(department_id) ON DELETE SET NULL
                    )
                    """
    )
     conn.commit()
     print("Instructor table created successfully")
     conn.close()

departments()
courses()
enrollments()
grades()
instructors()


