var http = require('http');
var mysql = require('mysql');

// Add the credentials to access your database
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : '',
    database : 'hospital'
});

// connect to mysql


// Perform a query

// Close the connection


http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('SQL query printed in terminal');

   

    


    $query = 'SELECT * FROM OT';

	connection.query($query, function(err, rows, fields) {

	    console.log("Query succesfully executed: ", rows);

	});
    

}).listen(8080);



/*var http = require('http');
var mysql = require('mysql');

// Add the credentials to access your database
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'root',
    password : '',
    database : 'hospital'
});

// connect to mysql


// Perform a query

// Close the connection


http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('Hello World!');
    connection.connect(function(err) {
    // in case of error
    if(err){
        console.log(err.code);
        console.log(err.fatal);
    }

    $query = 'SELECT * FROM OT';

	connection.query($query, function(err, rows, fields) {
	    if(err){
	        console.log("An error ocurred performing the query.");
	        return;
	    }

	    console.log("Query succesfully executed: ", rows);
	});


	});

    

	connection.end(function(){
    // The connection has been closed
	});

}).listen(8080);/*
