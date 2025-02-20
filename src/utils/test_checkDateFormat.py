import unittest
from utils.checkDateFormat import checkDateFormat


class TestCheckDateFormat(unittest.TestCase):

    def test_valid_date_format(self):
        result = checkDateFormat("2023-10-10")
        self.assertTrue(result)

    def test_invalid_date_format(self):
        result = checkDateFormat("invalid-date")
        self.assertEqual(
            result,
            "Error: Invalid date format. Please use YYYY-MM-DD")

    def test_empty_date_string(self):
        result = checkDateFormat("")
        self.assertEqual(
            result,
            "Error: Invalid date format. Please use YYYY-MM-DD")

    def test_incorrect_date_format(self):
        result = checkDateFormat("10-10-2023")
        self.assertEqual(
            result,
            "Error: Invalid date format. Please use YYYY-MM-DD")


if __name__ == '__main__':
    unittest.main()
