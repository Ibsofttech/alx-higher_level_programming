#!/usr/bin/node

const occur = parseInt(process.argv[2]);
if (isNaN(occur)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < occur; x++) {
    console.log('C is fun');
  }
}
