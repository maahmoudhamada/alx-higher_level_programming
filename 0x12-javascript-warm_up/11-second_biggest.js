#!/usr/bin/node

const array = process.argv.slice(2);
const len = array.length;
let tmp;

if (len === 0 || len === 1) {
  console.log(0);
} else {
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (array[j] > array[j + 1]) {
        tmp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = tmp;
      }
    }
  }
  console.log(array[len - 2]);
}
