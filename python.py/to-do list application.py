def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Complete")
    print("4. View Tasks")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

def remove_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task removed.")
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{index}. {task['task']} - {status}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
