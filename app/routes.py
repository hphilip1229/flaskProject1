from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    user = {"name":"Jeffron","favGame":"Debugger"} 
    return render_template('index.html', user=user)

@app.route('/secret')
def secret():
    return render_template('secret.html')
@app.route('/sush')
def sush():
    return "<h1> AHHHHHH!!<h1>"
@app.route('/sendBreakfast', methods =['GET','POST']) 
def sendBreakfast():
    if request.method == 'GET':
        return "You didnt fill out the form and I bet u say route weirdly. "
    else:
        userData = dict(request.form)
        nickname = userData['nickname'][0]
        nickname = model.shout(nickname)
        breakfast = userData['breakfast'][0]
        breakfast = model.shout(breakfast) 
        return render_template("breakfast.html", nickname=nickname, breakfast=breakfast)