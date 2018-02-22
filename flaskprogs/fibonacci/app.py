from flask import Flask
#from fib import calcfib
app = Flask(__name__)

@app.route('/')
def home():
    val=fib(11)
    return str(val)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    app.run()



'''
db = MySQLdb.connect("localhost","root","","hospital" )
    cursor = db.cursor()
    if request.method == 'POST':
    	username=request.form['username']
    	password=request.form['password']
    	cursor.execute("SELECT username FROM users WHERE username = %s and password = %s", (username, password))
    	rownum=cursor.rowcount;
        if rownum!=1:
            error = 'Invalid Credentials. Please try again.'
        else:
        	error = 'Successful!'













 if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        	error = 'Successful!'
            #return redirect(url_for('home'))
'''