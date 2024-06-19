#!/usr/bin/node

const OriginalSq = require('./5-square.js');

module.exports = class Square extends OriginalSq {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let shape = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          shape += 'C';
        }
        if (i + 1 !== this.height) {
          shape += '\n';
        }
      }
      console.log(shape);
    }
  }
};
