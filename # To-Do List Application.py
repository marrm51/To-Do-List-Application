# To-Do List Application

# List to store tasks
tasks = []

# Function to display the menu
def display_menu():
    print("\n--- To-Do List Application ---")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Quit")
    print("----------------------------")

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    if task.strip():  # Check if the task is not empty after removing spaces
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")  # The else follows the if block correctly

# Function to view all tasks
def view_tasks():
    if tasks:  # If there are tasks in the list
        print("\n--- Task List ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")  # The else follows the if block correctly

# Function to delete a task
def delete_task():
    if tasks:  # If there are tasks to delete
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully.")
            else:
                print("Invalid task number.")  # The else follows the if block correctly
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No tasks to delete.")  # The else follows the if block correctly

# Main function to run the application
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a number between 1 and 4.")
        finally:
            print("Returning to the main menu...")

# Run the application
if __name__ == "__main__":
    main()
     