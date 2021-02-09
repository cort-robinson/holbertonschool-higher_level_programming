#!/usr/bin/node

const baseSquare = require('./5-square');
module.exports = class Square extends baseSquare {
  charPrint (c = 'X') {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
