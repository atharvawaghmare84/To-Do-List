#-------------------------------------------------------------------------------
# Name:       Atharva Waghmare
# Purpose:    TASK 1
#
# Author:      atharva
#
# Created:     14-07-2023
# Copyright:   (c) athar 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def display_todo_list(todo_list):

    if not todo_list:
        print("To-Do List is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {'[X]' if task['completed'] else '[ ]'} {task['task']}")

def add_task(todo_list, task):
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the to-do list.")

def mark_task_completed(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        todo_list[task_index - 1]["completed"] = True
        print(f"Task {task_index} marked as completed.")
    else:
        print("Invalid task index!")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task['task']}' removed from the to-do list.")
    else:
        print("Invalid task index!")

def main():
    todo_list = []

    while True:
        print("\nOptions:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            mark_task_completed(todo_list, task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
