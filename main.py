########################################################################################
######################          Import packages      ###################################
########################################################################################
from google.cloud import storage
from flask import Blueprint, render_template, flash,send_file
from flask_login import login_required, current_user

from __init__ import create_app, db
from datetime import datetime
import time
import pytz
import json
import numpy as np
import json
import pandas as pd
from ast import literal_eval


########################################################################################
# our main blueprint
main = Blueprint('main', __name__)
storage_client = storage.Client.from_service_account_json('bucket_key.json')
bucket = storage_client.get_bucket('fbspendbucket')

blob = bucket.get_blob('FBReport.json')
json_data = blob.download_as_string()

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route("/today")
def today():
    datas = literal_eval(json_data.decode('utf8'))
    today=[]
    for data in datas:
#        print(datas)
        value='today'
        if value in data.values():
#            print(datas)
            today.append(data)
            TodayExcelDF = pd.DataFrame(today)
            # TodayExcelDF.to_csv('CSVExport/today.csv')
# update on date
        key="Current_Date"
        if key in data:
            date=(data[key])
            
    return render_template("today.html",updateOn=date, dataToday=today)


#Download Today Excel
@main.route("/today_file")
def today_file():
    excel = "CSVExport/today.csv"
    return send_file(excel, as_attachment=True)



@main.route("/yesterday")
def yesterday():
    datas = literal_eval(json_data.decode('utf8'))
    yesterday=[]
    for data in datas:
        value='yesterday'
        if value in data.values():
            yesterday.append(data)
            YestExcelDF = pd.DataFrame(yesterday)
            # YestExcelDF.to_csv('CSVExport/yesterday.csv')
# update on date
        key="Current_Date"
        if key in data:
            date=(data[key])            
    return render_template("yesterday.html",updateOn=date, dataYesterday=yesterday )

#Download Today Excel
@main.route("/yesterday_file")
def yesterday_file():
    Yestexcel = "CSVExport/yesterday.csv"
    return send_file(Yestexcel, as_attachment=True)



@main.route("/this_month")
def this_month():
    datas = literal_eval(json_data.decode('utf8'))
    this_month=[]
    for data in datas:
        value='this_month'
        if value in data.values():
#                print(ReportData)
            this_month.append(data)
            this_monthExcelDF = pd.DataFrame(this_month)
            # this_monthExcelDF.to_csv('CSVExport/this_month.csv')
# update on date
        key="Current_Date"
        if key in data:
            date=(data[key])    
    return render_template("this_month.html",updateOn=date, datathis_month=this_month )

#Download This Month Excel
# @main.route("/this_month_file")
# def this_month_file():
#     This_month_excel = "CSVExport/this_month.csv"
#     return send_file(This_month_excel, as_attachment=True)


@main.route("/last_month")
def last_month():
    datas = literal_eval(json_data.decode('utf8'))
    last_month=[]
    for data in datas:
        value='last_month'
        if value in data.values():
#                print(ReportData)
            last_month.append(data)
            last_monthExcelDF = pd.DataFrame(last_month)
            # last_monthExcelDF.to_csv('CSVExport/last_month.csv')
# update on date
        key="Current_Date"
        if key in data:
            date=(data[key])    
    return render_template("last_month.html",updateOn=date, datalast_month=last_month )

#Download This Month Excel
@main.route("/last_month_file")
def last_month_file():
    Last_month_excel = "CSVExport/last_month.csv"
    return send_file(Last_month_excel, as_attachment=True)


@main.route("/maximum")
def maximum():
    datas = literal_eval(json_data.decode('utf8'))
    maximum=[]
    for data in datas:
        value='maximum'
        if value in data.values():
#                print(ReportData)
            maximum.append(data)
            MaximumMonthsExcelDF = pd.DataFrame(maximum)
            # MaximumMonthsExcelDF.to_csv('CSVExport/Maximum_months.csv')
# update on date
        key="Current_Date"
        if key in data:
            date=(data[key])    
    return render_template("maximum.html",updateOn=date, datamaximum=maximum )

#Download 37 Month Excel
@main.route("/Maximum_months_file")
def Maximum_months_file():
    Maximum_month_excel = "CSVExport/Maximum_months.csv"
    return send_file(Maximum_month_excel, as_attachment=True)    



app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode