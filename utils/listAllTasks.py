import json


def listAllTasks(tasks_list):
    print(json.dumps(tasks_list, indent=4))
