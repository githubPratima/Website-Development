import csv
import os

import calc.MyCalc
from base_model import db
from flask import Blueprint, request, render_template, flash, url_for
from flask_login import current_user
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.utils import redirect

from .models import SimpleHistory

c = calc.MyCalc.AdvMyCalc()  # here the state is persisted between requests (note it may be shared across users)
mycalc = Blueprint('mycalc', __name__, url_prefix='/mycalc')


@mycalc.route('/history', methods=['GET'])
def get_history():
    if not current_user.is_anonymous:
        results = SimpleHistory.query.filter_by(user_id=current_user.id).order_by(SimpleHistory.created.desc()).limit(
            5).all()
        print(results)
    else:
        results = []
    return render_template("calc_history.html", history=results)


@mycalc.route('/delete/<history_id>', methods=['POST'])
def delete_single_history(history_id):
    if not current_user.is_anonymous:
        try:
            sh = db.session.query(SimpleHistory).filter_by(id=history_id).delete()
            db.session.commit()
            print(f"Deleted history {sh}")
            flash("History deleted", "success")
        except SQLAlchemyError as e:
            print(e)
            flash(str(e), "error")
            db.session.rollback()
    else:
        print("Not authorized")
        flash("Not authorized to delete other user history", "error")
    return redirect(url_for("mycalc.get_history"))


@mycalc.route('/delete', methods=['POST'])
def delete():
    if not current_user.is_anonymous:
        try:
            sh = db.session.query(SimpleHistory).filter_by(user_id=current_user.id).delete()
            db.session.commit()
            print("Deleted all history for this user")
            flash("All history of user deleted", "success")
        except SQLAlchemyError as e:
            print(e)
            flash(str(e), "error")
            db.session.rollback()
    else:
        print("Not authorized")
        flash("Not authorized to delete other user history", "error")
    return redirect(url_for("mycalc.get_history"))


@mycalc.route('/upload', methods=['GET', 'POST'])
def upload_csv():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print(uploaded_file.filename)
        uploaded_file.save(uploaded_file.filename)
        try:
            with open(uploaded_file.filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                        line_count += 1
                    else:
                        r = c.calc(row[0], row[2], row[1])
                        stored_eq = str(row[0] + row[2] + row[1])
                        sh = SimpleHistory(eq=stored_eq, result=r, user_id=current_user.id)
                        db.session.add(sh)
                        try:
                            db.session.commit()
                            print("Recorded calculation history")
                            flash("Recorded calculation history", "success")
                        except SQLAlchemyError as e:
                            print(e)
                            flash(str(e), "error")
                            db.session.rollback()
                        # TODO pass data to calculator to run/execute and add to history
        except Exception as e:
            print('An exception occurred: {}'.format(e))
        finally:
            os.remove(uploaded_file.filename)
            print("Deleted uploaded file")
    return redirect(url_for("mycalc.do_calc"))


@mycalc.route('/adv_upload', methods=['GET', 'POST'])
def upload_adv_csv():
    uploaded_file = request.files['adv_file']
    adv_functions = {
        "mean": "1",
        "median": "2",
        "mode": "3",
        "std dev": "4",
        "z score": "5"
    }
    if uploaded_file.filename != '':
        print(uploaded_file.filename)
        print(request.form['advMode'])
        print("Hello")
        uploaded_file.save(uploaded_file.filename)
        try:
            with open(uploaded_file.filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                advMode = request.form['advMode']
                # line_count = 0
                # if line_count == 0:
                #     print(f'Column names are {", ".join(row)}')
                #     line_count += 1
                # else:
                input_numbers = c.read_stats_file(uploaded_file.filename)
                print(input_numbers[str(f"{advMode}")])
                print("Before Try Calc")
                r = c.stats_calc(input_numbers[str(f"{advMode}")], adv_functions[f"{advMode}"], mode=1)
                stored_eq = str(input_numbers[str(f"{advMode}")])
                sh = SimpleHistory(eq=stored_eq, result=r, user_id=current_user.id)
                db.session.add(sh)
                try:
                    db.session.commit()
                    print("Recorded calculation history")
                    flash("Recorded calculation history", "success")
                except SQLAlchemyError as e:
                    print(e)
                    flash(str(e), "error")
                    db.session.rollback()
                    # TODO pass data to calculator to run/execute and add to history
        except Exception as e:
            print('An exception occurred: {}'.format(e))
            flash('An exception occurred: {}'.format(e), "error")
        finally:
            os.remove(uploaded_file.filename)
            print("Deleted uploaded file")
    return redirect(url_for("mycalc.do_calc"))


@mycalc.route('/', methods=['GET', 'POST'])
def do_calc():
    # c = calc.MyCalc.AdvMyCalc() # here the state resets each time
    data = request.form
    iSTR = data.get("eq")
    advMode = data.get("advMode")
    loadHistory = data.get("loadHistory", 0, type=int) > 0
    if iSTR or advMode is not None:
        checks = calc.MyCalc.AdvMyCalc.ops
        adv_functions = {
            "mean": "1",
            "median": "2",
            "mode": "3",
            "std dev": "4",
            "z score": "5"
        }
        r = "UNSUPPORTED"
        if loadHistory:
            r = data.get("result")
            c.ans = c._as_number(r)
        else:
            for check in checks:
                if check in iSTR:
                    nums = iSTR.split(check)
                    if nums[0] == '':
                        nums[0] = "ans"
                    try:
                        r = c.calc(nums[0].strip(), check, nums[1].strip())
                        print("R is " + str(r))
                    except:
                        r = "ERROR"
                    if not current_user.is_anonymous:
                        sh = SimpleHistory(eq=iSTR, result=r, user_id=current_user.id)
                        db.session.add(sh)
                        try:
                            db.session.commit()
                            print("Recorded calculation history")
                            flash("Recorded calculation history", "success")
                        except SQLAlchemyError as e:
                            print(e)
                            flash(str(e), "error")
                            db.session.rollback()
                    return render_template("my_calc.html", result=r, eq=iSTR)
            if advMode in adv_functions:
                parsed_data = iSTR.split(",")
                print(parsed_data)
                print(adv_functions[f"{advMode}"])
                try:
                    r = c.stats_calc(parsed_data, adv_functions[f"{advMode}"], 1)
                except:
                    r = "ERROR"
                if not current_user.is_anonymous:
                    sh = SimpleHistory(eq=iSTR, result=str(r), user_id=current_user.id)
                    db.session.add(sh)
                    try:
                        db.session.commit()
                        print("Recorded calculation history")
                        flash("Recorded calculation history", "success")
                    except SQLAlchemyError as e:
                        print(e)
                        flash(str(e), "error")
                        db.session.rollback()
                print(r)
                return render_template("my_calc.html", result=r, eq=iSTR)
            else:
                print("Comma separated values can only be used for advanced calculations")
        print("The action you tried is not supported, please try again")
        return render_template("my_calc.html", result=r, eq=iSTR)
    return render_template("my_calc.html")