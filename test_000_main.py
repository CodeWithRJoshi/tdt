import unittest

from os import listdir
import os


class MainTest(unittest.TestCase):
    def test_all_(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        py_files = (f for f in listdir(dir_path) if f.endswith('.' + 'py'))
        py_files = set(py_files)

        code_files = {x for x in py_files if not x.startswith('test_')}
        test_files_test = {x for x in py_files if x.startswith('test_')}
        test_files = {x.lstrip('test_') for x in test_files_test}

        self.assertEqual(code_files, test_files)


def main():
    unittest.main()


if __name__ == "__main__":
    main()

##################
# Sample Error
##################

# FAIL: test_all_ (__main__.MainTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_000_main.py", line 17, in test_all_
#     self.assertEqual(code_files, test_files)
# AssertionError: Items in the first set but not the second:
# '000_main_2.py'
# Items in the second set but not the first:
# '000_main.py'
