import unittest
import io
import sys
import unittest.mock


def func(n):
    total = 0
    # print(n)
    for i in range(n):
        v = input("Give me someting: ")
        total += int(v)
        print(v)


class TestModule(unittest.TestCase):
    # Can;t use @staticmethod as it can't be called from patch,but it won't have an object so have to initialize self to None!
    def getdata(self=None):
        # May return a dictionary/tuple if multiple things are required!
        # Or use a second parameter and return based on that!
        return [1, 2, 3, 0]

    @unittest.mock.patch('builtins.input', side_effect=getdata())
    def test_func_list1(self, mock=None):
        test_data = self.getdata()
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        # stream_handler.stream = sys.stdout
        # logger.addHandler(stream_handler)
        func(len(test_data))  # Call function.

        sys.stdout = sys.__stdout__  # Reset redirect.
        # Now works as before.
        # print(capturedOutput, type(capturedOutput))
        outputList = capturedOutput.getvalue().split('\n')
        outputList = [int(el) for el in outputList if len(el) > 0]
        t = 0
        for i, x in enumerate(outputList):
            self.assertEqual(x, test_data[i])


if __name__ == "__main__":
    unittest.main()
