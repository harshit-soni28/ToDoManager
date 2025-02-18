def deleteTask(task_list, taskNumber):

    if (taskNumber < 1 or taskNumber > len(task_list)):
        print("Invalid task Number")
        return

    task_to_delete = None

    for task in task_list:
        if task['task_number'] == taskNumber:
            task_to_delete = task

    if task_to_delete is None:
        print("Selected task number does not exist")
        return

    task_list.remove(task_to_delete)
    print(f"Task with taskId {taskNumber} deleted: {task_to_delete}")
    return task_list
