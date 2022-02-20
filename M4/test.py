#Homework date 02/20/2022 UCID=pp235

import unittest
from MyCalc import MyCalc
class TestCalculator(unittest.TestCase):
  def setUp(self):
    self.MyCalc = MyCalc()

  def test_add(self):
    self.assertEqual(self.MyCalc.add(2, 7), 9)
    self.assertEqual(self.MyCalc.add("ans", 7), 16)
    self.assertEqual(self.MyCalc.add(1, 4), 5)
    self.assertEqual(self.MyCalc.add("ans", 7), 12)


  def test_subtract(self):
    self.assertEqual(self.MyCalc.sub(20, 5), 15)
    self.assertEqual(self.MyCalc.sub("ans", 5), 10)

  def test_multiply(self):
    self.assertEqual(self.MyCalc.mult(2, 2), 4)
    self.assertEqual(self.MyCalc.mult("ans", 2), 8)

  def test_divide(self):
    self.assertEqual(self.MyCalc.div(25, 5), 5)
    self.assertEqual(self.MyCalc.div("ans", 5), 1)
