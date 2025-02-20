import unittest
from io import StringIO
import sys
from utils.listAllTasks import listAllTasks
import json
# filepath: /home/harshit.soni/Desktop/ToDoProject/utils/test_listAllTasks.py


class TestListAllTasks(unittest.TestCase):

    def setUp(self):
        self.task_list = [
            {"task_number": 1, "description": "Task 1",
             "dueDate": "2023-10-10", "completed": False},
            {"task_number": 2, "description": "Task 2",
             "dueDate": "2023-10-11", "completed": False},
        ]

    def test_list_all_tasks_empty(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        listAllTasks([])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "[]")

    def test_list_all_tasks_with_tasks(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        listAllTasks(self.task_list)
        sys.stdout = sys.__stdout__
        expected_output = json.dumps(self.task_list, indent=4)
        self.assertEqual(captured_output.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
