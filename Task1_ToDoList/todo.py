# Task 1: To-Do List Application
# Author: DHARMESH J
# Date: 02/06/2025

# This to-do list app was made by me (Dharmesh J) during the CodSoft internship.
# I wrote this after learning how Python lists and functions work.

tasks = []

def add_task():
    """Adds a new task to the to-do list."""
    task = input("Enter a new task: ")
    tasks.append({'task': task, 'completed': False})
    print(f"✅ Task '{task}' added successfully.")

def view_tasks():
    """Displays all tasks in the to-do list with their completion status."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print(f"\n📋 Your To-Do List (Total: {len(tasks)} tasks):")
        for index, task in enumerate(tasks, start=1):
            status = "[✅]" if task["completed"] else "[❌]"
            print(f"{index}. {status} {task['task']}")

# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_task()

    elif choice == '2':
        view_tasks()

    elif choice == '3':
        view_tasks()
        if tasks:
            try:
                task_num = int(input("Enter the task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    print(f"✅ Task '{tasks[task_num - 1]['task']}' marked as completed.")
                else:
                    print("⚠ Invalid task number.")
            except ValueError:
                print("⚠ Please enter a valid number.")
        else:
            print("No tasks to mark.")

    elif choice == '4':
        print("👋 Exiting the To-Do List application. Goodbye!")
        break

    else:
        print("⚠ Invalid choice. Please try again.")