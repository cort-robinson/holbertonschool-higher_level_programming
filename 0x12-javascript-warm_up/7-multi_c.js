#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  for (let x = 1; x <= process.argv[2]; x++) {
    console.log('C is fun');
  }
}
