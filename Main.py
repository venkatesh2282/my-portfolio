# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    print()

def delete_student():
    view_students()
    index = int(input("Enter student number to delete: ")) - 1
    
    if 0 <= index < len(students):
        students.pop(index)
        print("Student deleted successfully!\n")
    else:
        print("Invalid choice\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")
