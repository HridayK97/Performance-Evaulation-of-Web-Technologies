from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

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