#!/usr/bin/node

function factorial (n) {
  if (n === 1) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}

const args = process.argv.slice(2);
const num = Math.floor(args[0]);
if (Number.isNaN(num)) {
  console.log(1);
} else {
  const result = factorial(num);
  console.log(result);
}
