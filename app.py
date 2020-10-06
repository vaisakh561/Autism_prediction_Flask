from flask import Flask, render_template, request
from flask_debug import Debug

from sqlalchemy.orm import sessionmaker

import numpy as np
import pickle
import pandas as pd



app = Flask(__name__)



@app.route("/")
def index():
    return render_template("home.html")


@app.route("/place")
def place():
    return render_template("place.html")



@app.route('/placefind',methods = ['POST','GET'])
def placefind():
    if request.method == 'POST':
        s = request.form['cities']

    df = pd.read_excel('input/Book1.xlsx')

    dis = []
    for i,j in df.iterrows():
        if s== j['HOSPITAL_LOCATION']:
            m = j['HOSPITAL_NAME'],j['HOSPITAL_ADDRESS'],j['HOSPITAL_PHONENO'],j['HOSPITAL_LOCATION']
            dis.append(m)
    return render_template("list.html",u=dis)

@app.route('/predict',methods = ['POST'])
def predict():
    ui = []
    
    if request.method == 'POST':
        ui.append(int(request.form['q1']))
        ui.append(int(request.form['q2']))
        ui.append(int(request.form['q3']))
        ui.append(int(request.form['q4']))
        ui.append(int(request.form['q5']))
        ui.append(int(request.form['q6']))
        ui.append(int(request.form['q7']))
        ui.append(int(request.form['q8']))
        ui.append(int(request.form['q9']))
        ui.append(int(request.form['q10']))
        ui.append(int(request.form['q11']))
        ui.append(int(request.form['q12']))
        ui.append(int(request.form['q13']))
        ui.append(int(request.form['q14']))
        ui.append(int(request.form['q15']))
        print("its come to 1 if")
    print(ui)
    


    l=[]

    for i in ui:
        l.append(i)
    l1=[]
    l1.append(l)
    print(l1)

    rfc=pickle.load(open('rf_train_model.sav', 'rb'))

    result = rfc.predict(l1)
    print(result)


    if result==1:
        res="The child may have Autism Spectrum Disorder"
    else:
        res="The child does't have Autism Spectrum Disorder"
    return render_template('result.html',u=res,re=result)

if __name__ == '__main__':
    app.run(debug=True)
