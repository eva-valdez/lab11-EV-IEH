
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 4), -8)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(4, 20), 5)
        self.assertAlmostEqual(divide(3, 10), 10 / 3)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     fill in code
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)
        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
