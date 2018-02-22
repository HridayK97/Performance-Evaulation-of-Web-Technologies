#!c:/python36/python.exe

import MySQLdb




print("Content-Type: text/html")


print()
'''
print ("""
    <TITLE>CGI script ! Python</TITLE>
    <H1>This is my first CGI script</H1>
    Hello, world!
""")
'''


# Open database connection
db = MySQLdb.connect("localhost","root","","hospital" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM OT"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      rid = row[0]
      roomno = row[1]
      # Now print fetched result
      print ("rid=%d,roomno=%d <br>" % \
             (rid, roomno))
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()