from flask import Blueprint, request, render_template

from calc.MyCalc import MyCalc

c=MyCalc()
mycalc = Blueprint('mycalc', __name__, url_prefix='/mycalc')

@mycalc.route('/', methods=['GET'])
def view_calc():
    return render_template("my_calc.html", result="")

@mycalc.route('/', methods=['POST'])
def do_calc():
    #c = calc.MyCalc.AdvMyCalc() # here the state resets each time
    checks = c.ops
    print(c.ops)
    data = request.form
    iSTR = data.get("eq")
    try:
        for check in checks:
            if check in iSTR:
                nums = iSTR.split(check)
                print(nums)
                try:
                    r = c.calc(check,nums[0].strip(), nums[1].strip())

                    print("R is " + str(r))
                except:
                    r = ""

                return render_template("my_calc.html", result=r)
            return render_template("my_calc.html", result="UNSUPPORTED", eq=iSTR)
    except Exception as e:
        print(e)
        r = "ERROR"
    return render_template("my_calc.html", result=r, eq=iSTR)