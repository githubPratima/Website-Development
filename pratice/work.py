import csv

import pytest

from M4.mycal import MyCalc

def grab_test_file2():
    with open("std"
              ".csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows



@pytest.mark.parametrize(argnames=("name","v1","v2","v3","v4","v5", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])




def test_csvstd_dev(name,v1,v2,v3,v4,v5,ea):
    calc = MyCalc()
    arr = [v1,v2,v3,v4,v5]
    r = calc.std_dev(arr)
    if name == "positive":
        assert r == MyCalc._as_number(ea)
    else:
        assert r != MyCalc._as_number(ea)



def grab_test_file2():
    with open("mean.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows



@pytest.mark.parametrize(argnames=("name","v1","v2","v3","v4","v5", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])




def test_csvmean(name,v1,v2,v3,v4,v5,ea):
    calc = MyCalc()
    arr = [v1,v2,v3,v4,v5]
    r = calc.mean(arr)
    if name == "positive":
        expected = round(calc._as_number(ea))
        result = round(r)
        if name == "positive":
           assert result == expected

    else:
        assert r != calc._as_number(ea)



 def mode(self, L):
        modecount = 0
        for i in range(len(L)):
            icount = self._as_number(L.count(L[i]))
            if icount > modecount:
                mode = self._as_number(L[i])
                modecount = icount    #this is the codes to find out the mode.
        return mode