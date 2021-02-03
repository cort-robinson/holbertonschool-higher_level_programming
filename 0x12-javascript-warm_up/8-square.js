#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let x = 1; x <= process.argv[2]; x++) {
    for (let y = 1; y <= process.argv[2]; y++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
