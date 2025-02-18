
def markComplete(task_list, task_id):
    if task_id < 1 or task_id > len(task_list):
        print("Invalid task Number")
        return task_list

    for task in task_list:
        if task['task_number'] == task_id:
            task['completed'] = True
            print(f"Task with taskId {task_id} status updated to True")
            return task_list
    print("Task not found")
    return task_list
