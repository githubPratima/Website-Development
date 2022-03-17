class MyCalc:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 + num2
        return self.ans

    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 - num2
        return self.ans

    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 * num2
        return self.ans

    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1 / num2
        return self.ans


    def mean(L):
        total = 0
        for x in L:
            total += x
        mean = total / len(L)
        return mean

    def median(L):
        L.sort()
        if len(L) % 2 != 0:
            median = L[int(len(L) / 2)]
        else:
            median = L[(int(len(L) / 2)) - 1] + L[int(len(L) / 2)]
            median = median / 2
        return median

    def mode(L):
        counter = 0
        num = L[0]

        for i in L:
            curr_frequency = L.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = i
            if len(set(L)) == len(L):
                return 'there is no mode'

        return num

    def variance(data):
        n = len(data)
        mean = sum(data) / n
        deviations = [(x - mean) ** 2 for x in data]
        variance = sum(deviations) / n
        return variance

    def std_dev(ls):
        n = len(ls)
        mean = sum(ls) / n
        var = sum((x - mean) ** 2 for x in ls) / n
        std_dev = var ** 0.5
        return std_dev

    number_list = []

    while (True):
        ask = input('enter a number and say "stop" to end: ')
        if ask == 'stop':
            break
        number_list.append(int(ask))

    mean = str(mean(number_list))
    median = str(median(number_list))
    mode = str(mode(number_list))
    variance = str(variance(number_list))
    std_dev = str(std_dev(number_list))

    print(
        'mean: ' + mean + '\n' + 'median: ' + median + '\n' + 'mode: ' + mode + '\n' + 'variance: ' + variance + '\n' + 'std_dev: ' + std_dev + '\n')


if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done before - check to hanlde negative values
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done last so negative numbers work
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                elif "median" in iSTR:
                    nums = iSTR.split("median")[1].split(",")  # assumes a comma list of values for median
                    r = calc.median(nums)
                    # etc






    else:

        print("Good bye")
        is_running = False