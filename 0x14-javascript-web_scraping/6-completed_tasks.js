#!/usr/bin/node
// A Script To Read The Content of A File

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }

  const completedTasks = {};
  body.forEach((element) => {
    if (element.completed) {
      if (!completedTasks[element.userId]) {
        completedTasks[element.userId] = 1;
      } else {
        completedTasks[element.userId] += 1;
      }
    }
  });

  console.log(completedTasks);
});
