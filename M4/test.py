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

  def test_addition(self):
    self.assertEqual(self.MyCalc.add(2, 5), 7)
    self.assertEqual(self.MyCalc.add("ans", 5), 12)
    self.assertEqual(self.MyCalc.add(4, 5), 9)
    self.assertEqual(self.MyCalc.add("ans", 2), 11)

  def test_division(self):
    self.assertEqual(self.MyCalc.div(25, 5), 5)
    self.assertEqual(self.MyCalc.div("ans", 5), 1)
    self.assertEqual(self.MyCalc.div(20, 4), 5)
    self.assertEqual(self.MyCalc.div("ans", 5), 1)

  def test_substract(self):
    self.assertEqual(self.MyCalc.sub(20, 5), 15)
    self.assertEqual(self.MyCalc.sub("ans", 5), 10)
    self.assertEqual(self.MyCalc.sub(6, 4), 2)
    self.assertEqual(self.MyCalc.sub("ans", 1), 1)

