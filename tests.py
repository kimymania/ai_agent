import unittest

# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python import run_python_file


class TestFileGetter(unittest.TestCase):
    def test1(self):
        result = run_python_file("calculator", "main.py")
        self.assertTrue(result, result.startswith("Error: "))
        print(result)

    def test2(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        self.assertTrue(result, result.startswith("Error: "))
        print(result)

    def test3(self):
        result = run_python_file("calculator", "tests.py")
        self.assertTrue(result, result.startswith("Error: "))
        print(result)

    def test4(self):
        result = run_python_file("calculator", "../main.py")
        self.assertTrue(result, result.startswith("Error: "))
        print(result)

    def test5(self):
        result = run_python_file("calculator", "nonexistent.py")
        self.assertTrue(result, result.startswith("Error: "))
        print(result)


if __name__ == "__main__":
    unittest.main()
