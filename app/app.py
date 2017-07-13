from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///sebodb.db', echo=True)
 
app = Flask(__name__)
# Views
@app.route('/')
def home_page():
    if session.get('logged_in'):
        return dash_page()
    else:
        return render_template('index.html')

		
@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['email'])
        POST_PASSWORD = str(request.form['password'])
	 
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.email.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
        result = query.first()
        if result:
            session['logged_in'] = True
            return redirect(url_for('dash_page'))
        else:
            flash('wrong password!')
        return home_page()

    return render_template('login_boot.html')

@app.route('/dashboard')
def dash_page():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
    session['logged_in'] = False
    print ("Saindo")
    return redirect(url_for('home_page'))

@app.route('/sign-up', methods = ['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        # create a Session
        Session = sessionmaker(bind=engine)
        session = Session()
 
        user = User(str(request.form['name']), str(request.form['email']), str(request.form['password']))
        session.add(user)
        session.commit()
		
        return redirect(url_for('home_page'))
		
    return render_template('sign-up.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0',port=4000, debug = False)
