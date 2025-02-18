# ToDoManager

## Overview
ToDoManager is a simple command-line application for managing tasks. It allows users to add new tasks, mark tasks as complete, delete tasks, and list all tasks.

## Features
- Add new tasks with a description and due date.
- Mark tasks as complete.
- Delete tasks.
- List all tasks.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ToDoProject.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ToDoProject
    ```
3. Install the required dependencies (if any).

## Usage
Run the application:
```sh
python3 src/main.py
```
Follow the on-screen prompts to manage your tasks.

## Project Structure
```
ToDoProject/
├── src/
│   ├── main.py
│   ├── utils/
│   │   ├── addNewTask.py
│   │   ├── markComplete.py
│   │   ├── deleteTask.py
│   │   ├── listAllTasks.py
│   │   ├── state.py
│   │   └── checkDateFormat.py
├── README.md
```

## Modules
- `addNewTask.py`: Contains the function to add a new task.
- `markComplete.py`: Contains the function to mark a task as complete.
- `deleteTask.py`: Contains the function to delete a task.
- `listAllTasks.py`: Contains the function to list all tasks.
- `state.py`: Maintains the state of tasks and task numbers.
- `checkDateFormat.py`: Contains the function to check the date format.

## Examples
```
1. Add new task
2. Mark task as complete
3. Delete task
4. List all tasks
5. Exit
Enter your choice: 1
Enter task description: Buy groceries
Enter due date: 2025-02-20
Task Added Successfully.
```
## License
This project is licensed under the MIT License.

