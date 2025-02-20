import unittest
from utils.markComplete import markComplete

# filepath: /home/harshit.soni/Desktop/ToDoProject/utils/test_markComplete.py


class TestMarkComplete(unittest.TestCase):

    def setUp(self):
        self.task_list = [
            {"task_number": 1, "description": "Task 1",
             "dueDate": "2023-10-10", "completed": False},
            {"task_number": 2, "description": "Task 2",
             "dueDate": "2023-10-11", "completed": False},
        ]

    def test_mark_complete_success(self):
        result = markComplete(self.task_list, 1)
        self.assertTrue(self.task_list[0]["completed"])
        self.assertEqual(result, self.task_list)

    def test_mark_complete_invalid_task_id(self):
        result = markComplete(self.task_list, 3)
        self.assertFalse(self.task_list[0]["completed"])
        self.assertFalse(self.task_list[1]["completed"])
        self.assertEqual(result, self.task_list)

    def test_mark_complete_non_existent_task_id(self):
        result = markComplete(self.task_list, 5)
        self.assertFalse(self.task_list[0]["completed"])
        self.assertFalse(self.task_list[1]["completed"])
        self.assertEqual(result, self.task_list)

    def test_mark_complete_empty_task_list(self):
        empty_task_list = []
        result = markComplete(empty_task_list, 1)
        self.assertEqual(result, empty_task_list)


if __name__ == '__main__':
    unittest.main()
