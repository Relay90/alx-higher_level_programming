#!/usr/bin/node
// function that returns the number of occurrences in a list

const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map((e, index) => e * index);
console.log(mappedList);
