#!/usr/bin/node
// A Script To Read The Content of A File

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    console.log(content.title);
  }
});
