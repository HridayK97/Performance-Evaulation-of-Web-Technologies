# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from dbconnect import connection
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    c, conn = connection()
	c.execute("SELECT * FROM OT")
    return "error"  # return a string
    

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()