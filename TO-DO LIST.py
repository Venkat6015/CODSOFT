tasks = []

def add_task():
    task = {}
    task['name'] = input("Enter task name: ")
    task['due_date'] = input("Enter due date (YYYY-MM-DD): ")
    task['priority'] = input("Enter priority (high/medium/low): ")
    task['completed'] = False
    tasks.append(task)
    print("Task added!")

def list_tasks():
    print("Task list:")
    for i, task in enumerate(tasks, start=1):
        status = "completed" if task['completed'] else "not completed"
        print(f"{i}. {task['name']} - {task['due_date']} - {task['priority']} - {status}")

def update_task():
    task_id = int(input("Enter task number to update: ")) - 1
    if 0 <= task_id < len(tasks):
        task = tasks[task_id]
        task['name'] = input("Enter new task name: ")
        task['due_date'] = input("Enter new due date (YYYY-MM-DD): ")
        task['priority'] = input("Enter new priority (high/medium/low): ")
        print("Task updated!")
    else:
        print("Invalid task number.")

def delete_task():
    task_id = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def mark_task_complete():
    task_id = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        print("Task marked complete!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Quit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task_complete()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
