from datetime import timedelta
from flask import Flask,render_template,request,session,make_response,session

app = Flask(__name__)

app.secret_key = "sina"


@app.route('/')
def mainpage():
    if session.get('user_email'):
        return f'Welcome! Your email is {session['user_email']}'
    else:
        return render_template('form.html')

@app.route('/Submit',methods=["POST"])
def submit_user():
    try:
        email = request.form["email"]
        # password = request.form["password"]

        response = make_response('<h1>Your email successfully saved on network. <a href="/">Return to home page</a></h1>')
        session['user_email'] = email
        session.permanent = True
        app.permanent_session_lifetime = timedelta(days=1)

        return response
    except Exception as ex:
        return f"Error! : {ex}"
    
