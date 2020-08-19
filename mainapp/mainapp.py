from flask import Flask, render_template, request, redirect, url_for
from database.createproffy import createproffy
from database.db import init_sqlite, finish_sqlite
from pagesredirect_functions import  give_classes_function
from general_functions import convert_subject, convert_time_to_secs, query_proffy, filter_proffy, call_create_proffy
from data_structures import weekdays, subjects, define_proffy_values, define_class_values, define_class_schedule_values

app = Flask(__name__)


@app.route('/')
def index():    
    return render_template('index.html')


@app.route('/study', methods=["GET"])
def study():
    req = request.args  

    filters = {
        "subject": req.get("subject", type = int),
        "weekday": req.get("weekday", type = int),
        "time": req.get("time", type = str)
    }

    subject = filters["subject"]
    weekday = filters["weekday"]
    time = filters["time"]

    if not filters["time"]:
        app.logger.info("this query in sqlite must show all proffys")
        proffys_data = query_proffy()
    else:
        app.logger.info("this query in sqlite must show proffys filtered")
        proffys_data = filter_proffy(subject = subject, weekday = weekday, time = time)

    return render_template('study.html', proffys = proffys_data, subjects = subjects, weekdays = weekdays, filters = filters)


@app.route('/give-classes', methods=["GET", "POST"])
def give_classes():
    if request.method == "POST":
        req = request.form

        proffy_values = define_proffy_values(name = req["name"], avatar = req["avatar"], whatsapp = req["whatsapp"], bio = req["bio"])
        class_values = define_class_values(subject = req["subject"], cost = req["cost"])
        class_schedule_values = define_class_schedule_values(weekday = req.getlist("weekday[]"), time_from = req.getlist("time_from[]"), time_to = req.getlist("time_to[]"))
        
        call_create_proffy(proffy_values = proffy_values, class_values = class_values, class_schedule_values = class_schedule_values)
        
        return redirect(url_for('study'))
    else: # GET
        return render_template('give-classes.html', subjects = subjects, weekdays = weekdays)


@app.errorhandler(404)
def not_found(error):
    return "404 Not Found"  #TODO Create a HTML page to 404 Error


if __name__ == '__main__':
    app.run(debug = True)