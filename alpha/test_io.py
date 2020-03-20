import io
import sys
from unittest.mock import patch
from unittest import mock
import unittest


def yes_or_no():
    answer = input("Do you want to quit? > ")
    print('yo')
    if answer == "yes":
        return("Quitter!")
    elif answer == "no":
        return("Awesome!")
    else:
        return("BANG!")


class TestMePlease(unittest.TestCase):

    @patch('builtins.input', return_value='yes')
    def test_quitting(self, ip):
        self.assertEqual(yes_or_no(), "Quitter!")

    @patch('builtins.input', return_value='yes')
    def test_print(self, ip):
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        yes_or_no()  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        # Now works as before.
        self.assertEqual(capturedOutput.getvalue().strip(), 'yo')


if __name__ == "__main__":
    unittest.main()
