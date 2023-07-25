#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const file = process.argv[3];

request(process.argv[2], function (error, response, body) {
	  if ((error)) { console.log(error); } else {
		      fs.writeFile(file, body, 'utf-8', function (err) {
			            if ((err)) return console.log(err);
			          });
		    }
});
