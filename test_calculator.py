import unittest
from calculator import addition, subtraction, multiplication, division

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        """Test the addition function."""
        self.assertEqual(addition(3, 5), 8)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(-1, 8), 7)

    def test_subtraction(self):
        """Test the subtraction function."""
        self.assertEqual(subtraction(9, 2), 7)
        self.assertEqual(subtraction(0, 0), 0)
        self.assertEqual(subtraction(7, -10), 17)

    def test_multiplication(self):
        """Test the multiplication function."""
        self.assertEqual(multiplication(9, 2), 18)
        self.assertEqual(multiplication(10, 5), 50)
        self.assertEqual(multiplication(-7, 3), -21)

    def test_division(self):
        """Test the division function."""
        self.assertEqual(division(14, 2), 7)
        self.assertEqual(division(-7, 2), -3.5)
        self.assertEqual(division(9, 2), 4.5)

        with self.assertRaises(ValueError):
            division(10, 0)

if __name__ == '__main__':
    unittest.main()
