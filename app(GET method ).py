from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome' , methods=["GET"])
def saywelcome():
    email = request.args.get('email')
    password = request.args.get('password')

    return render_template('welcome.html',email=email,password=password)