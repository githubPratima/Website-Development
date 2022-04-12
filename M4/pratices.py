import csv

import pytest

from M4.MyCalc import MyCa
import csv

import pytest

from M4.MyCalc import MyCalc
def grab_test_file2():
    with open("random2.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows

# Option 1 https://stackoverflow.com/questions/45879028/pytest-parameterized-test-with-custom-id-function
@pytest.mark.parametrize(argnames=("name","v1","v2", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])
def test_csvmult(name, v1,v2, ea):
    calc = MyCalc()
    r = calc.mult(v1, v2)
    if name == "positive":
        assert r == int(ea)
    else:
        assert r != int(ea)


import csv

import pytest

from M4.MyCalc import MyCalc

def grab_test_file2():
    with open("std.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows



@pytest.mark.parametrize(argnames=("name","v1","v2","v3","v4","v5", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])




def test_csvsstd_dev(name,v1,v2,v3,v4,v5,ea):
    calc = MyCalc()
    arr = [v1,v2,v3,v4,v5]
    r = calc.sstd_dev(arr)
    if name == "positive":
        expected = round(calc._as_number(ea))
        result = round(r)
        if name == "positive":
           assert result == expected

    else:
        assert r != calc._as_number(ea)


import csv

import pytest

from M4.MyCalc import MyCalc

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




def test_csvsmean(name,v1,v2,v3,v4,v5,ea):
    calc = MyCalc()
    arr = [v1,v2,v3,v4,v5]
    r = calc.smean(arr)
    if name == "positive":
        expected = round(calc._as_number(ea))
        result = round(r)
        if name == "positive":
           assert result == expected

    else:
        assert r != calc._as_number(ea)


def grab_test_file2():
    with open("median.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows



@pytest.mark.parametrize(argnames=("name","v1","v2","v3","v4","v5", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])




def test_csvmedian(name,v1,v2,v3,v4,v5,ea):
    calc = MyCalc()

    arr = [v1,v2,v3,v4,v5]
    r = calc.median(arr)
    if name == "positive":
        expected = round(calc._as_number(ea))
        result = round(r)
        if name == "positive":
           assert result == expected

    else:
        assert r != calc._as_number(ea)


def grab_test_file2():
    with open("variance.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows



@pytest.mark.parametrize(argnames=("name","v1","v2","v3","v4","v5", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])




def test_csvsvariance(name,v1,v2,v3,v4,v5,ea):
    calc = MyCalc()
    arr = [v1,v2,v3,v4,v5]
    r = calc.svariance(arr)
    if name == "positive":
        expected = round(calc._as_number(ea))
        result = round(r)
        if name == "positive":
           assert result == expected

    else:
        assert r != calc._as_number(ea)


def grab_test_file2():
    with open("sqrt.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows

# Option 1 https://stackoverflow.com/questions/45879028/pytest-parameterized-test-with-custom-id-function
@pytest.mark.parametrize(argnames=("name","v1", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])
def test_csvsqrt(name, v1, ea):
    calc = MyCalc()
    r = calc.sqrt(v1)
    if name == "positive":
        assert r == int(ea)
    else:
        assert r != int(ea)


def grab_test_file2():
    with open("square.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        rows = []
        for row in csv_reader:
            if line_count > 0:
                rows.append(row)
            line_count += 1
        return rows

# Option 1 https://stackoverflow.com/questions/45879028/pytest-parameterized-test-with-custom-id-function
@pytest.mark.parametrize(argnames=("name","v1", "ea"),argvalues=grab_test_file2(), ids=[i[0] for i in grab_test_file2()])
def test_csvsquare(name, v1, ea):
    calc = MyCalc()
    r = calc.square(v1)
    if name == "positive":
        assert r == int(ea)
    else:
        assert r != int(ea)

import csv

import pytest

from M4.MyCalc import MyCalc

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
        expected = round(calc._as_number(ea))
        result = round(r)
        if name == "positive":

         assert result == expected

    else:
        assert r != calc._as_number(ea)
