from flask import Flask,redirect,render_template,request,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome' , methods=['POST'])
def saywelcome():
    email = request.form['email']
    password = request.form['password']

    return render_template('welcome.html',email=email,password=password)

