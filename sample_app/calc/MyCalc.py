
class MyCalc:
    ans = 0
    ops = ["+", "-", "x", "/", "square", "sqrt", "smean", "median", "sstd_dev", "mode", "svariance"]
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

    def calc(self, op, *in_nums):
        print(f"calc() {op} and {in_nums} {type(in_nums)}")
        print("Hello")
        # removed since this is solved in do_calc()
        # nums = in_nums[1].split(",")
        nums = list(in_nums)
        """print(f"nums after [1] split {nums}")
        if len(nums) == 0:
            nums = in_nums
            print(f"Regular list nums: {nums}")
        else:
            print(f"List from tuple nums: {nums}")
        print("Bye")"""


        if op == "+":
            #nums = in_nums
            print("add nums{}".format(nums))
            return self.add(nums[0],nums[1])
        elif op == "-":
            # = in_nums
            print("Hello")
            print("sub nums{}".format(nums))
            return self.sub(nums[0],nums[1])
        elif op == "/":
            #nums = in_nums
            print("div nums{}".format(nums))
            return self.div(nums[0],nums[1])
        elif op == "x":
            #nums = in_nums
            print("add mult{}".format(nums))
            return self.mult(nums[0],nums[1])
        elif op == "square":
            #nums.pop(0)
            print("square nums{}".format(nums))
            return self.square(*nums)
        elif op == "sqrt":
            #nums.pop(0)
            print("sqrt nums{}".format(nums))
            return self.sqrt(*nums)

        elif op == "smean":
             #nums.pop(0)
             print("smean nums{}".format(nums))
             return self.smean(*nums)
        elif op == "median":
            #nums.pop(0)
            print("median nums{}".format(nums))
            return self.median(*nums)
        elif op == "sstd_dev":
            #nums.pop(0)
            print("sstd_dev nums{}".format(nums))
            return self.sstd_dev(*nums)
        elif op == "mode":
            #nums.pop(0)
            print("mode nums{}".format(nums))
            return self.mode(*nums)
        elif op == "svariance":
            #nums.pop(0)
            print("svariance nums{}".format(nums))
            return self.svariance(*nums)




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


    def sqrt(self,N):
        if self._as_number(N) < 0:
            print('Square root of negative number does not exist!')
            return
        else:
            sqrt = self._as_number(N)**0.5  #this code gives square root of the number
            print('Square root of number {}: {}'.format(N,sqrt))
            return sqrt



    def square(self, n):
        if self._as_number(n) < 0:
            return
        else:
            return self._as_number(n) ** 2  #this code gives square of the number

    def smean(self, *in_data):
        data = list(in_data)
        print(data)
        n = len(data)
        for i in range(n):
            data[i] = self._as_number(data[i])
        smean = sum(data) / n
        return smean


    def median(self, *in_L):
        L= list(in_L)
        print(L)
        L.sort()
        lLen = len(L)
        half = int(lLen / 2)  #this code gives median of the numbers
        if lLen % 2 != 0:
            median = L[half]
        else:
            left = self._as_number(L[half - 1])
            right = self._as_number(L[half])
            # median = L[half - 1] + L[half]
            median = left + right
            median = median / 2
        return median


    def mode(self, *in_data):
        data = list(in_data)
        print(data)
        counts = {}
        for item in data:
            num = self._as_number(item)
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1  # These codes helps to find out the mode
        return counts


    def svariance(self, *in_data):
        data = list(in_data)
        print(data)
        n= len(data)
        for i in range(n):
            data[i] = self._as_number(data[i])
        mean = sum(data) / n

        deviations = [(self._as_number(x) - mean) ** 2 for x in data]
        svariance = sum(deviations) / n #this code gives us the sample variance of numbers.
        return svariance


    def sstd_dev(self, *in_ls):
        ls = list(in_ls)
        print(ls)
        n = len(in_ls)
        for i in range(len(ls)):
            ls[i] = self._as_number(ls[i])
        mean = sum(ls) / n
        var = sum((x - mean) ** 2 for x in ls) / n
        sstd_dev = var ** 0.5   #this code gives us the standard deviation of numbers.
        return sstd_dev





if __name__ == '__main__':

    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    ops = ["+", "-", "x", "/", "square", "sqrt", "smean", "median", "sstd_dev", "mode", "svariance"]
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

                elif "smean" in iSTR:
                    print("doing smean")
                    nums = iSTR.split("smean")[1].strip("[").strip("]").split(",")
                    print("nums after split")
                    print(nums)

                    r = calc.smean(nums)
                    print("R is " + str(r))


                elif "median" in iSTR:
                    print("doing median")
                    nums = iSTR.split("median")[1].strip("[").strip("]").split(",")  # assumes a comma list of values for median
                    r = calc.median(nums)
                    print("R is " + str(r))

                elif "mode" in iSTR:
                    print("doing mode")
                    nums = iSTR.split("mode")[1].strip("[").strip("]").split(",")
                    r = calc.mode(nums)
                    print("R is " + str(r))

                elif "sstd_dev" in iSTR:
                    print("doing sstd_dev")
                    nums = iSTR.split("sstd_dev")[1].strip("[").strip("]").split(",")
                    r = calc.sstd_dev(nums)
                    print("R is " + str(r))

                elif "svariance" in iSTR:
                    print("doing svariance")
                    nums = iSTR.split("svariance")[1].strip("[").strip("]").split(",")
                    r = calc.svariance(nums)
                    print("R is " + str(r))
                elif "sqrt" in iSTR:
                    nums = iSTR.split("sqrt")[1].strip("[").strip("]")
                    r = calc.sqrt(nums)
                    print("R is " + str(r))
                elif "square" in iSTR:
                    nums = iSTR.split("square")[1].strip("[").strip("]")
                    r = calc.square(nums)
                    print("R is " + str(r))

                    # etc

    else:

        print("Good bye")


