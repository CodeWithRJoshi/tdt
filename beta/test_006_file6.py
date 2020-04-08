import unittest
import unittest.mock

import importlib
import sys
from io import StringIO
from contextlib import redirect_stdout


class TestSimple(unittest.TestCase):
    side_effect = [1, 2, 3, 0]
    @unittest.mock.patch('builtins.input', side_effect=side_effect)
    def test_simple(self, mock):
        backup = sys.stdout
        op = StringIO()  # capture output
        with redirect_stdout(op):
            importlib.import_module('006_file6')
        output = op.getvalue()

        self.assertEqual(f"{self.side_effect[0]}\n",
                         output, f"You must print {self.side_effect[0]}")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
