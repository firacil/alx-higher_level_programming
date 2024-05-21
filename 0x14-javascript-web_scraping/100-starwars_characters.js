#!/usr/bin/node

const request = require('request');
const mid = process.argv[2];
const url = `https://swapi.dev/api/films/${mid}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  for (const c of characters) {
    request(c, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const cData = JSON.parse(body);
      console.log(cData.name);
    });
  }
});
