import unittest

# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


class TestFileGetter(unittest.TestCase):
    def test1(self):
        result = get_file_content("calculator", "main.py")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for current directory:\n{result}")

    def test2(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for 'pkg' directory:\n{result}")

    def test3(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for '/bin' directory:\n{result}")

    def test4(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for '../' directory:\n{result}")


if __name__ == "__main__":
    unittest.main()
