from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os
#from instagram import getfollowedby, getname


Login_1 = Flask(__name__)
Login_1.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(Login_1)
Login_1.config['static'] = '/static/'


class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"


#@Login_1.route('/', methods=['GET', 'POST'])
"""def home():
    if not session.get('logged_in'):
        full_filename = os.path.join(Login_1.config['static'], '1.jpeg')
        return render_template('Login.html', user_image = full_filename)
    else:
        if request.method == 'POST':
            username = getname(request.form['username'])
            full_filename = os.path.join(Login_1.config['static'], '1.jpeg')
            return render_template('SignUp.html', user_image = full_filename)
        return render_template('Login.html')
"""
@Login_1.route('/', methods=['GET', 'POST'])
@Login_1.route('/Login', methods=['GET', 'POST'])
def Login():
    """Login Form"""
    data_temp=None
    if request.method == 'GET':
        full_filename = os.path.join(Login_1.config['static'], '1.jpeg')
        return render_template('Login.html', user_image = full_filename)
    else:
        name = request.form['username']
        #passw = str(0 if request.form.get('chk1') is None else value)+str(0 if request.form.get('chk2') is None else value)+str(0 if request.form.get('chk3') is None else value)+str(0 if request.form.get('chk4') is None else value)+str(0 if request.form.get('chk4') is None else value)+str(0 if request.form.get('chk5') is None else value)+str(0 if request.form.get('chk6') is None else value)+str(0 if request.form.get('chk7') is None else value)+0 if request.form.get('chk8') is None else value)+str(0 if request.form.get('chk9') is None else value)
        count=1
        passw=""
        while(count<=9):
            if(request.form.get('chk'+str(count))):
                passw=passw+str(request.form.get('chk'+str(count)))
            count+=1
        #try:
        data = User.query.all()
        for i in data:
            if(name==i.username and passw==i.password):
                data_temp=1
                return "Login Successful"

        if data_temp is None:
            return 'Useranme or Password Incorrect'
        #except:
            #return "Not logged_in in_except"


@Login_1.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    """Register Form"""
    if request.method == 'POST':
        
        #passw = str(0 if request.form.get('chk1') is None else value)+str(0 if request.form.get('chk2') is None else value)+str(0 if request.form.get('chk3') is None else value)+str(0 if request.form.get('chk4') is None else value)+str(0 if request.form.get('chk4') is None else value)+str(0 if request.form.get('chk5') is None else value)+str(0 if request.form.get('chk6') is None else value)+str(0 if request.form.get('chk7') is None else value)+0 if request.form.get('chk8') is None else value)+str(0 if request.form.get('chk9') is None else value)
        count=1
        passw=""
        while(count<=9):
            if(request.form.get('chk'+str(count))):
                passw=passw+str(request.form.get('chk'+str(count)))
            count+=1
        new_user = User(username=request.form['username'],password=passw)
        db.session.add(new_user)
        db.session.commit()
        full_filename = os.path.join(Login_1.config['static'], '1.jpeg')
        return render_template('Login.html', user_image = full_filename)
    full_filename = os.path.join(Login_1.config['static'], '1.jpeg')    
    return render_template('SignUp.html',user_image = full_filename)


@Login_1.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


if __name__ == '__main__':
    Login_1.debug = True
    db.create_all()
    Login_1.secret_key = "123"
    Login_1.run(debug=True)