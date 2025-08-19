from flask import Flask,render_template,make_response,redirect,request,url_for

app = Flask(__name__)

@app.route('/')
def index():
    if request.cookies.get('user_email'):
        return f'Welcome!. Your email is {request.cookies['user_email']}'
    else:
        return render_template('form.html')

@app.route('/Submit',methods=["POST"])
def saywelcome():
    try:
        email = request.form['email']
        password = request.form['password']

        response = make_response('Your informations Successfully saved.<a href="/">return to home</a>')
        response.set_cookie('user_email' , email)
        return response
    except Exception as ex:
        return f'Error : {ex}'


