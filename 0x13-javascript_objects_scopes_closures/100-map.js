#!/usr/bin/node
const myList = require('./100-data.js').myList;
console.log(myList);
console.log(myList.map((item, index) => item * index));
