@mycalc.route('/upload', methods=['GET', 'POST'])
def upload_csv():
    checks = c.ops
    print(c.ops)
    data = request.form
    iSTR = data.get("eq")
        loadHistory = data.get("loadHistory", 0, type=int) > 0
    if iSTR is not None:
        r = "UNSUPPORTED"

    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print(uploaded_file.filename)
        uploaded_file.save(uploaded_file.filename)
        try:
            with open(uploaded_file.filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                for row in csv_reader:
                    print(f'Column names are {", ".join(row)}')
                    # TODO pass data to calculator to run/execute and add to history
        except Exception as e:
            print('An exception occurred: {}'.format(e))
        finally:
            os.remove(uploaded_file.filename)
            print("Deleted uploaded file")
    return redirect(url_for("mycalc.do_calc"))


@mycalc.route('/', methods=['GET', 'POST'])
def do_calc():
    # c = calc.MyCalc.AdvMyCalc()
    checks = c.ops
    print(c.ops)
    data = request.form
    iSTR = data.get("eq")
    loadHistory = data.get("loadHistory", 0, type=int) > 0
    if iSTR is not None:
        r = "UNSUPPORTED"
        if loadHistory:
            r = data.get("result")
            c.ans = c._as_number(r)
        else:
            for check in checks:
                print(str(checks) + " " + str(iSTR))
                if check in iSTR:
                    nums = iSTR.split(check)
                    print(nums)
                    try:
                        r = c.calc(check, *nums)
                        print("R is " + str(r))
                    except:
                        r = "ERROR"
                    if not current_user.is_anonymous:
                        sh = SimpleHistory(eq=iSTR, result=str(r), user_id=current_user.id)
                        db.session.add(sh)
                        try:
                            db.session.commit()
                            print("Recorded calculation history")
                            flash("Recorded calculation history ")
                        except SQLAlchemyError as e:
                            print(e)
                            flash(str(e), "error")
                            db.session.rollback()
                    return render_template("my_calc.html", result=r, eq=iSTR)
            print("The action you tried is not supported, please try again")
            return render_template("my_calc.html", result="UNSUPPORTED", eq=iSTR)
    return render_template("my_calc.html", result="")
