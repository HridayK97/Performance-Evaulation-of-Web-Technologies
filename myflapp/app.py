# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from dbconnect import connection
import hashlib
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    c, conn = connection()
    if request.method == 'POST':
    	username=request.form['username']
    	password=request.form['password']
    	hashpass=hashlib.md5(password.encode('utf-8')).hexdigest()

    	c.execute("SELECT username FROM users WHERE username = %s and hash = %s", (username, hashpass))
    	rownum=c.rowcount
    	if rownum==1:
    		error = 'Successful!'
    	else:
    		error = 'Invalid username or password. Try again'
    return render_template('login.html', error=error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()