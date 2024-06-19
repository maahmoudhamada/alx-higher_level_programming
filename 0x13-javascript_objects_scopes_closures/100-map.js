#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
const a = list.map(function (value, index) {
  return value * index;
});
console.log(a);
