#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (error, contents) {
	  if ((error)) { console.log(error); } else { process.stdout.write(contents); }
});
