# Function to display the to-do list
def display_tasks(tasks):
    if tasks:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in your to-do list.")

# Function to add a task to the to-do list
def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

# Function to remove a task from the to-do list
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            completed_task = tasks[task_num - 1] + " (Completed)"
            tasks[task_num - 1] = completed_task
            print(f"'{completed_task}' is now marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to manage the to-do list
def main():
    tasks = []
    while True:
        print("\nWhat would you like to do?")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                mark_completed(tasks)
            elif choice == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the main function
if __name__ == "__main__":
    main()
