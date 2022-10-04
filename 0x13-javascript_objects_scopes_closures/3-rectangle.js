#!/usr/bin/node
module.exports = class Rectaequal to 0 or not a positive integer, create emptyngle {
  constructor (w, h) {
    // If w or h is  object
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      if (i < this.height) { process.stdout.write('\n'); }
    }
  }
};
