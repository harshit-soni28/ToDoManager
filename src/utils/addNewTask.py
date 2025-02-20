import utils.state as state
from utils.checkDateFormat import checkDateFormat


def addNewTask(task_list, description, dueDate):
    if task_list is None:
        return "Task list cannot be None"

    try:
        date_validation = checkDateFormat(dueDate)
        if date_validation is not True:
            return date_validation

        if not description.strip():
            return "Please enter a description"

        task = {
            "task_number": state.task_number,
            "description": description,
            "dueDate": dueDate,
            "completed": False,
        }

        state.task_number += 1
        task_list.append(task)

        return "Task Added Successfully."

    except Exception as e:
        return f"An error occurred: {e}"
