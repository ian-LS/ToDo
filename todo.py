import json
import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['title']} - Due: {task.get('due_date', 'Not specified')}")

def add_task(tasks, title, due_date=None):
    task = {"title": title, "completed": False}
    if due_date:
        task["due_date"] = due_date
    tasks.append(task)
    print("Task added successfully.")

def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

def remove_completed_tasks(tasks):
    tasks = [task for task in tasks if not task["completed"]]
    print("Completed tasks removed.")
    return tasks

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove completed tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            due_date = input("Enter due date (optional, format YYYY-MM-DD): ")
            add_task(tasks, title, due_date)
            save_tasks(tasks)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as completed: "))
            complete_task(tasks, task_index)
            save_tasks(tasks)
        elif choice == "4":
            tasks = remove_completed_tasks(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
