#!/usr/bin/node

let count = 0;
exports.logMe = function (item) {
  function innerFunction () {
    console.log(`${count}: ${item}`);
    count++;
  }
  innerFunction();
};
