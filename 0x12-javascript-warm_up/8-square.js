#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);

if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
