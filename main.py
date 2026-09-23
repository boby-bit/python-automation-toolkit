from file_organizer import organize_files
from student_reports import generate_report
from task_manager import add_task, view_tasks
from data_analyzer import analyze_numbers

while True:
    print("\n=== LEVEL 4 BASIC ===")
    print("1. Organize Files")
    print("2. Student Report")
    print("3. Task Manager")
    print("4. Data Analyzer")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        path = input("Folder path: ")
        organize_files(path)

    elif choice == "2":
        name = input("Student Name: ")
        marks = list(map(int, input("Enter marks separated by space: ").split()))
        generate_report(name, marks)

    elif choice == "3":
        task = input("Enter task: ")
        add_task(task)
        view_tasks()

    elif choice == "4":
        nums = list(map(float, input("Enter numbers separated by space: ").split()))
        analyze_numbers(nums)

    elif choice == "5":
        break
