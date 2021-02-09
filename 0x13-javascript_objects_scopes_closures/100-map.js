#!/usr/bin/node

const list = require('./100-data').list;
const newList = [];
for (const index in list) {
  newList.push(list[index] * index);
}
console.log(list);
console.log(newList);
