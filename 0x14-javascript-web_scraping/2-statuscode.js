#!/usr/bin/node
// A Script To Read The Content of A File

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
