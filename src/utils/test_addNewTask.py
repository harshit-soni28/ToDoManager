import unittest
from utils.addNewTask import addNewTask
import utils.state as state


class TestAddNewTask(unittest.TestCase):

    def setUp(self):
        state.task_number = 1
        self.task_list = []

    def test_add_task_success(self):
        result = addNewTask(self.task_list, "Buy groceries", "2025-02-20")
        self.assertEqual(result, "Task Added Successfully.")
        self.assertEqual(len(self.task_list), 1)
        self.assertEqual(self.task_list[0]['description'], "Buy groceries")
        self.assertEqual(self.task_list[0]['dueDate'], "2025-02-20")
        self.assertEqual(self.task_list[0]['completed'], False)

    def test_add_task_invalid_date(self):
        result = addNewTask(self.task_list, "Buy groceries", "invalid-date")
        self.assertNotEqual(result, "Task Added Successfully.")
        self.assertEqual(len(self.task_list), 0)

    def test_add_task_empty_description(self):
        result = addNewTask(self.task_list, "", "2025-02-20")
        self.assertEqual(result, "Please enter a description")
        self.assertEqual(len(self.task_list), 0)

    def test_add_task_exception_handling(self):
        result = addNewTask(None, "Buy groceries", "2025-02-20")
        self.assertEqual(result, "Task list cannot be None")


if __name__ == '__main__':
    unittest.main()
