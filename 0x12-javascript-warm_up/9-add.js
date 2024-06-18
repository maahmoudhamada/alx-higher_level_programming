#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return (result);
}

const args = process.argv.slice(2);
const a = Math.floor(args[0]);
const b = Math.floor(args[1]);

console.log(add(a, b));
