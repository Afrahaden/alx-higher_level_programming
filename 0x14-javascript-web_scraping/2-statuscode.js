#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
	  if ((error)) { return console.log('code:', response && response.statusCode); }
	  console.log('code:', response && response.statusCode);
});
