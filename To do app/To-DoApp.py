tasks = []


def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


while True:
    print("\nOptions: add / show / remove / quit")
    action = input("Choose action: ").lower()

    if action == "add":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif action == "show":
        show_tasks()
    elif action == "remove":
        show_tasks()
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid number.")
    elif action == "quit":
        print("Bye!")
        break
    else:
        print("Invalid action.")
