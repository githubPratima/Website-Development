def test_subtract(self):
    self.assertEqual(self.MyCalc.sub(20, 5), 15)
    self.assertEqual(self.MyCalc.sub("ans", 5), 10)


def test_multiply(self):
    self.assertEqual(self.MyCalc.mult(2, 2), 4)
    self.assertEqual(self.MyCalc.mult("ans", 2), 8)
    self.assertEqual(self.MyCalc.mult(3, 3), 9)
    self.assertEqual(self.MyCalc.mult("ans", 3), 27)


def test_divide(self):
    self.assertEqual(self.MyCalc.div(25, 5), 5)
    self.assertEqual(self.MyCalc.div("ans", 5), 1)
