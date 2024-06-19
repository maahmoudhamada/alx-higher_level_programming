#!/usr/bin/node

module.exports = class Rectangle {
  validator (w, h) {
    if (w > 0 && h > 0) {
      return 1;
    } else {
      return 0;
    }
  }

  constructor (w, h) {
    if (this.validator(w, h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shape = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        shape += 'X';
      }
      if (i + 1 !== this.height) {
        shape += '\n';
      }
    }
    console.log(shape);
  }
};
