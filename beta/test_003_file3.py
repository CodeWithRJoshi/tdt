import unittest
import importlib
file1 = importlib.import_module('001_file1')


class TestSimple(unittest.TestCase):
    def test_addition_01(self):
        op = file1.addition(1, 2, 3)
        self.assertEqual(op, 6)

    def test_addition_02(self):
        args = (1, 2, 3, 'apple')
        self.assertRaises(TypeError, file1.addition, args)

    def test_addition_03(self):
        # file1.addition()
        args = None
        self.assertRaises(TypeError, file1.addition, args)

    def test_substract_01(self):
        op = file1.substract(10, 5)
        self.assertEqual(op, 5)

    def test_substract_02(self):
        op = file1.substract(3, 0)
        self.assertEqual(op, 3)

    def test_substract_03(self):
        op = file1.substract(28, 37)
        self.assertEqual(op, -9)

    def test_substract_04(self):
        args = (1, 2, 3, 'apple')
        self.assertRaises(TypeError, file1.substract, args)

    def test_substract_05(self):
        args = ()
        self.assertRaises(TypeError, file1.substract, args)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
