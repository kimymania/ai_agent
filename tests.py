import unittest

from functions.get_files_info import get_files_info


class TestFileGetter(unittest.TestCase):
    def test1(self):
        result = get_files_info("calculator", ".")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for current directory:\n{result}")

    def test2(self):
        result = get_files_info("calculator", "pkg")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for 'pkg' directory:\n{result}")

    def test3(self):
        result = get_files_info("calculator", "/bin")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for '/bin' directory:\n{result}")

    def test4(self):
        result = get_files_info("calculator", "../")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for '../' directory:\n{result}")


if __name__ == "__main__":
    unittest.main()
