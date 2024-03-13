#!/usr/bin/node
// Script that concatenates two files

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./concat-files.js file1 file2 output');
  process.exit(1);
}

const [, , file1, file2, output] = process.argv;

try {
  const contentA = fs.readFileSync(file1, 'utf-8');
  const contentB = fs.readFileSync(file2, 'utf-8');
  fs.writeFileSync(output, contentA + contentB);
  console.log(`Files ${file1} and ${file2} concatenated to ${output}`);
} catch (err) {
  console.error('Error:', err.message);
  process.exit(1);
}
