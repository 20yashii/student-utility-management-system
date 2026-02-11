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


# ----------- VALIDATION FUNCTIONS -----------

def get_valid_age():
    while True:
        age_input = input("Age: ")
        try:
            age = int(age_input)
            if age <= 0:
                print("❌ Age must be a positive number.")
            else:
                return age
        except ValueError:
            print("❌ Please enter a valid number for age.")


def get_valid_email():
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    while True:
        email = input("Email: ")
        if re.match(pattern, email):
            return email
        else:
            print("❌ Invalid email format. Try again.")


create_table()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = get_valid_age()  # ✅ validated age
        course = input("Course: ")
        email = get_valid_email()  # ✅ validated email

        add_student(name, age, course, email)
        print("Student added successfully!")

    elif choice == "2":
        students = view_students()
        for s in students:
            print(s)

    elif choice == "3":
        sid = int(input("Enter Student ID: "))
        print(search_student(sid))

    elif choice == "4":
        sid = int(input("Enter Student ID: "))
        name = input("New Name: ")
        age = get_valid_age()  # ✅ validated age
        course = input("New Course: ")
        email = get_valid_email()  # ✅ validated email

        update_student(sid, name, age, course, email)
        print("Student updated!")

    elif choice == "5":
        sid = int(input("Enter Student ID: "))
        delete_student(sid)
        print("Student deleted!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")


