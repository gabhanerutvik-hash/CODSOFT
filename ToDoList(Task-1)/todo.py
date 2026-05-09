tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


while True:
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_task = input("Enter task: ")
        tasks.append(new_task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if len(tasks) > 0:
            remove_num = int(input("Enter task number to remove: "))
            
            if 1 <= remove_num <= len(tasks):
                removed_task = tasks.pop(remove_num - 1)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice. Please try again.")
