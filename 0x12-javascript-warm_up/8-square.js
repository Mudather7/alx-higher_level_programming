#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
const character = 'X';
let i = 0;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (i < num) {
    console.log(character.repeat(num));
    i++;
  }
}
