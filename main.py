from database import create_table
from student import *

def menu():
    print("\nStudent Utility Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

create_table()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        email = input("Email: ")
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
        age = int(input("New Age: "))
        course = input("New Course: ")
        email = input("New Email: ")
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
