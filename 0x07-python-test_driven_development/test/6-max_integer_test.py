import unittest
from your_module import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])
        with self.assertRaises(TypeError):
            max_integer("123")

if __name__ == '__main__':
    unittest.main()
