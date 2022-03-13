import csv #ucid= pp235 : 3/13/2022 : I am trying to test the modes
import pytest
from M4.mycal import MyCalc
def grab_test_file2():
    with open("mode.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows
@pytest.mark.parametrize(argnames=("name","v1","v2","v3","v4","v5", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])
def test_csvmode(name,v1,v2,v3,v4,v5,ea):
    calc = MyCalc()
    arr = [v1,v2,v3,v4,v5]
    r = calc.mode(arr)
    if name == "positive":
         #assert r == calc._as_number(ea)
         assert r[2] == int(ea) #positve

    else:
        #assert r != calc._as_number(ea) # negative
        assert r != int(ea)
