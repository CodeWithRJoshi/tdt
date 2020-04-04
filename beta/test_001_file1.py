import unittest
import importlib
file1 = importlib.import_module('001_file1')


class TestSimple(unittest.TestCase):
    def test_simple_01(self):
        ip = 2
        exp_op = 2
        op = file1.simple(ip)
        self.assertEqual(exp_op, op+1)

    def test_simple_02(self):
        ip = 2
        exp_op = 2
        op = file1.simple2(ip)
        self.assertEqual(op, None)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
