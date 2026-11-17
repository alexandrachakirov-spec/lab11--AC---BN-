# https://github.com/alexandrachakirov-spec/lab11--AC---BN-
# Partner 1: Alexandra Chakirov
# Partner 2: Branden Neveau

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(12, 5), 17)
        self.assertEqual(add(-5, 5), 0)

    def test_subtract(self):
        self.assertEqual(subtract(0, 12), -12)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(7, 0), 7)


    ######## Partner 1

    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 7), 0)

    def test_div(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(4, 20), 5)
        self.assertAlmostEqual(div(3, 10), 10 / 3)


    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 4), 2)
        self.assertEqual(logarithm(2, 0.5), -1)
        self.assertEqual(logarithm(3, 27), 3)

    def exp(a, b):
        return a ** b

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 2)

    ######## Partner 1

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()