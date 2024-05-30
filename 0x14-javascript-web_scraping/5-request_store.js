#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    fs.writeFile(filename, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
