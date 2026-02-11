from database import create_table
from student import *
import re   # for email validation


def menu():
    print("\nStudent Utility Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def get_valid_age():
    while True:
        age_input = input("Age: ")
        try:
            age = int(age_input)
            if age <= 0:
                print("Age must be a positive number.")
            else:
                return age
        except ValueError:
            print("Please enter a valid number for age.")


def get_valid_email():
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input("Email: ")
        if re.match(pattern, email):
            return email
        else:
            print("Invalid email format. Try again.")


create_table()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = get_valid_age()
        course = input("Course: ")
        email = get_valid_email()

        add_student(name, age, course, email)
        print("Student added successfully!")

    elif choice == "2":
        students = view_students()

        if students:
            print("\n===== Student List =====")
            for s in students:
                print(f"""
Student ID : {s[0]}
Name       : {s[1]}
Age        : {s[2]}
Course     : {s[3]}
Email      : {s[4]}
------------------------------
""")
        else:
            print("No students found.")
        elif choice == "3":
    try:
        sid = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID! Please enter a numeric value.")
        continue

    try:
        student = search_student(sid)

        if student:
            print(f"""
Student ID : {student[0]}
Name       : {student[1]}
Age        : {student[2]}
Course     : {student[3]}
Email      : {student[4]}
------------------------------
""")
        else:
            print("Student not found.")

    except Exception as e:
        print("Error while searching student:", e)







