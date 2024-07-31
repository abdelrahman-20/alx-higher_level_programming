#!/usr/bin/node
// A Script To Read The Content of A File

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
