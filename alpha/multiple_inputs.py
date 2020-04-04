import unittest
import unittest.mock

# from mymodule import func


def func(n):
    total = 0
    for i in range(n):
        v = input("Give me someting: ")
        total += int(v)
        print(v)


class TestModule(unittest.TestCase):
    side_effect = [1, 2, 3, 0]
    @unittest.mock.patch('builtins.input', side_effect=side_effect)
    def test_func_list1(self, mock):
        self.assertEqual(func(len(side_effect)), 6)

    side_effect = [0]
    @unittest.mock.patch('builtins.input', side_effect=side_effect)
    def test_func_list2(self, mock):
        self.assertEqual(func(len(side_effect)), 0)


if __name__ == "__main__":
    unittest.main()
