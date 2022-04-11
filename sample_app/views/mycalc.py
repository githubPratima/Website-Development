from flask import Blueprint, request, render_template
import calc.MyCalc

c = calc.MyCalc.MyCalc()  # here the state is persisted between requests (note it may be shared across users)
mycalc = Blueprint('mycalc', __name__, url_prefix='/mycalc')

@mycalc.route('/', methods=['GET'])
def view_calc():
    return render_template("my_calc.html")


@mycalc.route('/', methods=['POST'])
def do_calc():
    # c = calc.MyCalc.AdvMyCalc() # here the state resets each time
    data = request.form
    iSTR = data.get("eq")
    try:
        if "+" in iSTR:
            nums = iSTR.split("+")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.add(nums[0].strip(), nums[1].strip())
            print("R is " + str(r))
        elif "/" in iSTR:
            nums = iSTR.split("/")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.div(nums[0].strip(), nums[1].strip())
            print("R is " + str(r))
        elif "*" in iSTR or "x" in iSTR:
            nums = iSTR.split("*")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.mult(nums[0].strip(), nums[1].strip())
            print("R is " + str(r))
        elif "-" in iSTR:
            nums = iSTR.split("-")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.sub(nums[0].strip(), nums[1].strip())
            print("R is " + str(r))
        elif "smean" in iSTR:
            nums = iSTR.split("smean")[1].strip("[").strip("]").split(",")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.smean(nums)
            print("R is " + str(r))
        elif "median" in iSTR:
            nums = iSTR.split("median")[1].strip("[").strip("]").split(",")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.median(nums)
            print("R is " + str(r))
        elif "mode" in iSTR:
            nums = iSTR.split("mode")[1].strip("[").strip("]").split(",")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.mode(nums)
            print("R is " + str(r))
        elif "sstd_dev" in iSTR:
            nums = iSTR.split("sstd_dev")[1].strip("[").strip("]").split(",")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.sstd_dev(nums)
            print("R is " + str(r))
        elif "svariance" in iSTR:
            nums = iSTR.split("svariance")[1].strip("[").strip("]").split(",")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.svariance(nums)
            print("R is " + str(r))
        elif "sqrt" in iSTR:
            nums = iSTR.split("sqrt")[1].strip("[").strip("]").split(",")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.sqrt(nums)
            print("R is " + str(r))
        elif "square" in iSTR:
            nums = iSTR.split("square")[1].strip("[").strip("]").split(",")
            if nums[0] == '':
                nums[0] = "ans"
            r = calc.square(nums)
            print("R is " + str(r))
        else:
            print("The action you tried is not supported, please try again")
            return render_template("my_calc.html", result="UNSUPPORTED", eq=iSTR)
    except Exception as e:
        print(e)
        r = ""
    return render_template("my_calc.html", result=r, eq=iSTR)
