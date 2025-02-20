import unittest
from utils.deleteTask import deleteTask

# filepath: /home/harshit.soni/Desktop/ToDoProject/utils/test_deleteTask.py
import utils.state as state


class TestDeleteTask(unittest.TestCase):

    def setUp(self):
        state.task_number = 1
        self.task_list = [
            {"task_number": 1, "description": "Task 1",
             "dueDate": "2023-10-10",
             "completed": False},
            {"task_number": 2, "description": "Task 2",
             "dueDate": "2023-10-11",
             "completed": False},
        ]

    def test_delete_task_success(self):
        deleteTask(self.task_list, 1)
        self.assertEqual(len(self.task_list), 1)
        self.assertEqual(self.task_list[0]["task_number"], 2)

    def test_delete_task_invalid_task_number(self):
        deleteTask(self.task_list, 3)
        self.assertEqual(len(self.task_list), 2)

    def test_delete_task_non_existent_task_number(self):
        deleteTask(self.task_list, 5)
        self.assertEqual(len(self.task_list), 2)

    def test_delete_task_from_empty_list(self):
        empty_task_list = []
        deleteTask(empty_task_list, 1)
        self.assertEqual(len(empty_task_list), 0)


if __name__ == '__main__':
    unittest.main()
