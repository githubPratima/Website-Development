#Homework date 02/20/2022 UCID=pp235

import unittest
from MyCalc import MyCalc
class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.MyCalc = MyCalc()

  def test_multiply(self):
    self.assertEqual(self.MyCalc.mult(2, 5), 10)
    self.assertEqual(self.MyCalc.mult("ans", 5), 50)
    self.assertEqual(self.MyCalc.mult(4, 5), 20)
    self.assertEqual(self.MyCalc.mult("ans", 2), 40)
