#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('undefined'.concat(' is ', process.argv[3]));
} else {
  console.log(process.argv[2].concat(' is ', process.argv[3]));
}
