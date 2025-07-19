import unittest

# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
from functions.write_file import write_file


class TestFileGetter(unittest.TestCase):
    def test1(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for current directory:\n{result}")

    def test2(self):
        result = write_file(
            "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
        )
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for current directory:\n{result}")

    def test3(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        self.assertTrue(result, result.startswith("Error: "))
        print(f"Result for current directory:\n{result}")


if __name__ == "__main__":
    unittest.main()
