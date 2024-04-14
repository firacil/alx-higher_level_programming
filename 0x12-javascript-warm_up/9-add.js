#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

if (isNaN(n1) || isNaN(n2)) {
  console.log('NaN');
} else {
  console.log(add(n1, n2));
}
