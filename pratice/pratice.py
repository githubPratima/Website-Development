
nums = iSTR.split("+")
r = calc.add(nums[0].strip(), nums[1].strip())
nums = iSTR.split("/")
r = calc.div(nums[0].strip(), nums[1].strip())
nums = iSTR.split("*")
r = calc.mult(nums[0].strip(), nums[1].strip())
nums = iSTR.split("-")
r = calc.sub(nums[0].strip(), nums[1].strip())
nums = iSTR.split("smean")[1].strip("[").strip("]").split(",")
r = calc.smean(nums)
nums = iSTR.split("median")[1].strip("[").strip("]").split(",")
r = calc.median(nums)
nums = iSTR.split("mode")[1].strip("[").strip("]").split(",")
r = calc.mode(nums)
nums = iSTR.split("sstd_dev")[1].strip("[").strip("]").split(",")
r = calc.sstd_dev(nums)
nums = iSTR.split("svariance")[1].strip("[").strip("]").split(",")
r = calc.svariance(nums)
nums = iSTR.split("sqrt")[1].strip("[").strip("]").split(",")
r = calc.sqrt(nums)
nums = iSTR.split("square")[1].strip("[").strip("]").split(",")
r = calc.square(nums)



def calc(iSTR):
  for x in iSTR:
    print(x.strip("[").strip("]").split(","))
all = ["add", "div", "mult", "div", "smean", "median", "mode", "sstd_dev", "variance"]
calc(all)



else:
print("The action you tried is not supported, please try again")
return render_template("my_calc.html", result="UNSUPPORTED", eq=iSTR)
except Exception as e:
print(e)
r = "ERROR"
return render_template("my_calc.html", result=r, eq=iSTR)
