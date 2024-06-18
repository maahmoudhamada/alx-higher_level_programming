#!/usr/bin/node

const args = process.argv.slice(2);
const x = Math.floor(args[0]);
let square = '';

if (Number.isNaN(x)) {
  console.log('Missing size');
} else if (x > 0) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    if ((i + 1) === x) {
      continue;
    }
    square += '\n';
  }
  console.log(square);
}
