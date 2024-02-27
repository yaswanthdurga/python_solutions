tasks = []

def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Your task '{task}' has been added to the list.")

def list_task():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def delete_task():
    list_task()
    try:
        task_to_delete = int(input("Choose the task to be deleted: "))
        if 1 <= task_to_delete <= len(tasks):
            removed_task = tasks.pop(task_to_delete - 1)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print(f"Task #{task_to_delete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    print("~~~ Welcome to the to-do-list Python application ~~~")
    
    while True:
        print("\n")
        print("Please select one of the following: ")
        print("---------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        print("----------------------------------------")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_task()
        elif choice == "4":
            break
        else:
            print("Please enter a valid input.")

    print("BYE.....BYE.....SEE YOU........👋👋👋")
