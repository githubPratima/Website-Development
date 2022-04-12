def calc(iSTR):
  for x in iSTR:
    print(x.strip("[").strip("]").split(","))
all = ["add", "div", "mult", "div", "smean", "median", "mode", "sstd_dev", "variance"]
calc(all)

