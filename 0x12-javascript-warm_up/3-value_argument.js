#!/usr/bin/node
// script that prints the first argument passed to it

console.log(process.argv[2] ? process.argv[2] : 'No argument');
