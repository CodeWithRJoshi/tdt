#! /bin/env python

import importlib
import os
from os import listdir
import sys
import time
import unittest
# from tdt.beta  import test_001_file1
# import test_001_file1
# try:
#     test_001_file1.main()
# except Exception as identifier:
#     pass


class MainTest(unittest.TestCase):
    def test_all_(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        py_files = (f for f in listdir(dir_path) if f.endswith('.' + 'py'))
        py_files = set(py_files)

        code_files = {x for x in py_files if not x.startswith('test_')}
        test_files_test = {x for x in py_files if x.startswith('test_')}
        test_files = {x.lstrip('test_') for x in test_files_test}

        # Cleanup for files that shouldn't be testsed!
        to_remove = ['__init__.py', '000_main.py']
        # test_to_remove = ['000_main.py']
        for f in to_remove:
            try:
                code_files.remove(f)
            except Exception as e:
                pass
                # print(e)

            try:
                test_files.remove(f)
            except Exception as e:
                pass
                # print(e)

        self.assertEqual(code_files, test_files)
        # tests = []
        print(dir_path)

        for tf in test_files:
            os.system("python" + " " + dir_path + "/test_" + tf)



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
