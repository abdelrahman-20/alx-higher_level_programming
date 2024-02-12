#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let x = process.argv[2];

  while (x--) {
    console.log('C is fun');
  }
}
