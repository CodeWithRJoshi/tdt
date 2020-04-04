#! /bin/env python
from io import StringIO  # Python 3

import importlib
import os
from os import listdir
import sys
import time
import unittest
import subprocess

def run(*args):
    return subprocess.run(['git'] + list(args), capture_output=True)

class MainTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MainTest, self).__init__(*args, **kwargs)
        self.UPDATED_LATER = {'cf13f5c', 'a33998d'}
        self.LAST_UPDATE = '802f071'
        self.BASE_PATH = os.path.dirname(os.path.realpath(__file__))

    class setUpClass():
        pass

    def test_all_(self):
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = self.BASE_PATH
        py_files = (f for f in listdir(dir_path) if f.endswith('.' + 'py'))
        py_files = set(py_files)

        code_files = {x for x in py_files if not x.startswith('test_')}
        test_files_test = {x for x in py_files if x.startswith('test_')}
        test_files = {x.lstrip('test_') for x in test_files_test}

        # Cleanup for files that shouldn't be testsed!
        to_remove = ['__init__.py']
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


    def test_get_new_files_only(self):
        file_list = set()


        #################################
        # Add untracked files to the list, for whatever reason  👨‍💻 !
        #################################

        # Add untracked file
        # def get_untrakced_files
        # untracked = get_untrakced_files()

        untracked_files = run('ls-files', '--others', '--exclude-standard')
        untracked_files = str(untracked_files.stdout, 'utf8')
        untracked_files = untracked_files.split('\n')
        untracked_files = [file for file in untracked_files if len(file.strip()) > 0]
        for u_f in untracked_files:
            file_list.add(os.path.abspath(u_f))

        #################################
        #################################

        # Nobody likes errors all the time
        # Only add the changed modified files for the test!


        STD_HASH = run("rev-list", "--ancestry-path", f"{self.LAST_UPDATE}..HEAD")

        UPDATED_LATER_FULL = set()
        for short_hash in self.UPDATED_LATER:
            long_hash = run("rev-parse", short_hash)
            long_hash = str(long_hash.stdout, 'utf8').strip()
            UPDATED_LATER_FULL.add(long_hash)



        STD_HASH  = str(STD_HASH.stdout,  'utf8')
        STD_HASH = STD_HASH.split('\n')
        STD_HASH = [h for h in STD_HASH if len(h) == 40] # It is 40 characters!
        HASH_TO_CHECK = [op for op in STD_HASH if not op in UPDATED_LATER_FULL]
        # print(len(STD_HASH), len(HASH_TO_CHECK))

        # for check in HASH_TO_CHECK:
        for check in HASH_TO_CHECK:
            files_modified = run('diff-tree', '--no-commit-id', '--name-only', '-r', check)
            # print(files_modified.stdout)

            files_modified = str(files_modified.stdout, 'utf8').strip()
            files_modified  = files_modified.split('\n')
            files_modified = [os.path.abspath(file) for file in files_modified]
            files_modified = [file for file in files_modified if file.startswith(self.BASE_PATH) and file.endswith('.py')]
            for file in files_modified:
                file_list.add(os.path.abspath(file))

            file_list = {os.path.basename(f).lstrip('test_') for f in file_list}



        # Cleanup for files that shouldn't be testsed!
        to_remove = ['000_main.py']
        # test_to_remove = ['000_main.py']
        for f in to_remove:
            try:
                file_list.remove(f)
            except Exception as e:
                pass
                # print(e)


        for tf in file_list:
            # print('Yoo!',tf)
            # py_script = f"{self.BASE_PATH}/test_{tf}"
            # op = exec(open(py_script).read())
            # print(op)
            # tf =
            # fil = importlib.import_module(f"{self.BASE_PATH}/test_{tf}")
            # op = fil.main()
            py_script = f"python {self.BASE_PATH}/test_{tf}"
            op = os.system(py_script)
            print("**",op)
            if op != 0:
                exit('Test failed, exiting...')


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
