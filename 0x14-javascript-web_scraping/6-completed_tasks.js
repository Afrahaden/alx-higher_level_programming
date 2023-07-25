#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
let counter = 0;

request(link, function (error, response, bd) {
	  const result = {};
	  if (error) {
		      return console.log(error);
		    } else {
			        const body = JSON.parse(bd);
			        while (counter < body.length) {
					      if (!result[body[counter].userId]) {
						              // result[body[counter].userId] = 0;
						      //         if (body[counter].completed === true) {
						      //                   result[body[counter].userId] = 1;
						      //                           }
						      //                                 } else {
						      //                                         if (body[counter].completed) {
						      //                                                   result[body[counter].userId] += 1;
						      //                                                           }
						      //                                                                 }
						      //                                                                       counter++;
						      //                                                                           }
						      //                                                                             }
						      //                                                                               console.log(result);
						      //                                                                               });
