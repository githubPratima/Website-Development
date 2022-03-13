def variance(data):
    n = len(data)

    mean = sum(data) / n

    deviations = [(x - mean) ** 2 for x in data]

    variance = sum(deviations) / n
    return variance

def stdev(data):
  import math
  var = variance(data)
  std_dev = math.sqrt(var)
  return std_dev


def square(self, num1, 2):
    if num1 == "ans":
        return self.square(self.ans, 2)
    else:
        num1 = self._as_number(num1)
        num2 = self._as_number(2)
        self.ans = num1 ** 2
    return self.ans

