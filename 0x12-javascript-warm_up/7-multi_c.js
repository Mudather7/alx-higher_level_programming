#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
let i = 0;
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i < argv[2]) {
    console.log('C is fun');
    i++;
  }
}
