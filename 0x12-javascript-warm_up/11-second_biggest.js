#!/usr/bin/node

// Script: 11-second_biggest.js

// Get the arguments from the command line
const args = process.argv.slice(2);

// If no arguments or only one argument is passed, print 0
if (args.length <= 1) {
    console.log(0);
} else {
    // Convert the arguments to integers and sort them in descending order
    const sortedIntegers = args.map(Number).sort((a, b) => b - a);

    // Print the second biggest integer
    console.log(sortedIntegers[1]);
}
