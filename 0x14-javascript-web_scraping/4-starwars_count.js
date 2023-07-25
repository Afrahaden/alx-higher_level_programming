#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
const actor = '/api/people/18/';
let counter = 0;
let result = 0;
request(link, function (error, response, body) {
	  if ((error)) { console.log(error); } else {
		      const results = JSON.parse(body).results;
		      for (counter = 0; counter !== results.length; counter++) {
			            if ((results[counter].characters.find(el => el.includes(actor)))) { result++; }
			          }
		      console.log(result);
		    }
});
