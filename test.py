# Simple To-Do List Application

def display_tasks(tasks):
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{index}. {task['name']} - {status}")

def add_task(tasks):
    """Add a new task to the list."""
    task_name = input("Enter the task name: ")
    tasks.append({'name': task_name, 'completed': False})
    print(f"Task '{task_name}' added.")

def complete_task(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    task_number = int(input("Enter the number of the task to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f"Task '{tasks[task_number - 1]['name']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    task_number = int(input("Enter the number of the task to remove: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['name']}' removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "_main_":
    main()