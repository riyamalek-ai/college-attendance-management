students = []

while True:
    print("\n--- Student Attendance Management System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Attendance Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter student name: ")

        student = {
            "roll": roll,
            "name": name,
            "present": 0,
            "total": 0
        }

        students.append(student)
        print("Student added successfully!")

    elif choice == "2":
        roll = input("Enter roll number: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                status = input("Enter P for Present or A for Absent: ").upper()

                if status == "P":
                    student["present"] += 1
                    student["total"] += 1
                    print("Present marked successfully!")
                elif status == "A":
                    student["total"] += 1
                    print("Absent marked successfully!")
                else:
                    print("Invalid attendance choice!")

                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "3":
        if len(students) == 0:
            print("No student records available.")
        else:
            for student in students:
                print("Roll No:", student["roll"])
                print("Name:", student["name"])
                print("Present:", student["present"])
                print("Total Classes:", student["total"])
                print("----------------------")

    elif choice == "4":
        roll = input("Enter roll number: ")
        found = False

        for student in students:
            if student["roll"] == roll:
                found = True

                if student["total"] == 0:
                    print("No attendance marked yet.")
                else:
                    percentage = (
                        student["present"] / student["total"]
                    ) * 100

                    print("Student:", student["name"])
                    print("Attendance:", round(percentage, 2), "%")

                break

        if not found:
            print("Student not found!")

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
