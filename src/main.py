from utils.addNewTask import addNewTask
from utils.markComplete import markComplete
from utils.deleteTask import deleteTask
from utils.listAllTasks import listAllTasks
import utils.state as state

while True:
    print("\n1. Add new task")
    print("2. Mark task as complete")
    print("3. Delete task")
    print("4. List all tasks")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        description = input("Enter task description: ")
        dueDate = input("Enter due date: ")
        print(addNewTask(state.tasks, description, dueDate))
    elif choice == 2:
        task_id = int(input("Enter task number to mark as complete: "))
        tasks = markComplete(state.tasks, task_id)
    elif choice == 3:
        task_id = int(input("Enter task number to delete: "))
        tasks = deleteTask(state.tasks, task_id)
    elif choice == 4:
        listAllTasks(state.tasks)
    elif choice == 5:
        break
    else:
        print("Invalid choice")
