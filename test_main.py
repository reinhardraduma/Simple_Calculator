""""
importing single_math_expression as it is where the actual calculations are done remember it also takes expression which is our input as an argument.
we use unittest.main at the end since any class that inherits from unittest.TestCase like in our case Testing SimpleCalc inherits, the methods within it
ie the functions mustr start with test. The naming convention any function that doesnt start with test isn't scanned. Did a demo with division _by _zero_test()
and it didnt run

"""
import unittest
from main import single_math_expression#

class TestingSimpleCalc(unittest.TestCase):

    def test_basic_maths(self):
        self.assertAlmostEqual(single_math_expression("5.0 + 9.1"),14.1,msg="addition")
        self.assertAlmostEqual(single_math_expression("5.0 - 9.1"),-4.1,msg="subtraction")
        self.assertAlmostEqual(single_math_expression("-5.0 * 9.1"),-45.5,msg="multiplication")
        self.assertAlmostEqual(single_math_expression("5.0 / 25"),0.2,msg="division")
        self.assertAlmostEqual(single_math_expression("(5 - 9)*4 + 3"), -13.0,msg="BODAMAS")
    

    def test_incomplete_expression(self):
        with self.assertRaises(Exception):
            single_math_expression("5.0 ^ ")

    def division_by_zero_test(self):#need to fix this tomorrow so that it works
        with self.assertRaises(ZeroDivisionError):
            single_math_expression("15 / 0")

    def test_remainder_modulo(self):
        self.assertAlmostEqual(single_math_expression("10 % 3"), 1.0)
        
    def test_power(self):
        self.assertAlmostEqual(single_math_expression("2^3"), 8.0)

#need to convert e.g 30 from radians tro degree as by default sympy uses radians
    # def test_trigonometric_expressions(self):
    #     self.assertAlmostEqual(single_math_expression("sin(30)"), 0.5)
    #     self.assertAlmostEqual(single_math_expression("cos(60)"), 0.5)
    #     self.assertAlmostEqual(single_math_expression("tan(60)"), 1.7321)
    #     self.assertAlmostEqual(single_math_expression("sinh(0.5)"), 30.0)
    #     self.assertAlmostEqual(single_math_expression("cosh(0.5)"), 60.0)
    #     self.assertAlmostEqual(single_math_expression("tanh(1.7321)"), 60.0)
                               

   
    
if __name__ == "__main__":
    unittest.main()
