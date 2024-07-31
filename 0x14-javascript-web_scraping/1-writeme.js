#!/usr/bin/node
// A Script To Read The Content of A File

const fs = require('fs');
const file = process.argv[2];
const data = process.argv[3];

fs.writeFile(file, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
