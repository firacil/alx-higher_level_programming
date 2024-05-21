#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tCompleted[todo.userId]) {
        tCompleted[todo.userId] = 1;
      } else {
        tCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tCompleted);
});
