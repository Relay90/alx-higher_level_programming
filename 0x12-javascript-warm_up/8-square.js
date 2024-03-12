#!/usr/bin/node

// Script: 8-square.js

// Get the size from the command line argument
const size = parseInt(process.argv[2]);

// Check if the size is a valid positive integer
if (isNaN(size) || size <= 0) {
    console.log("Missing size");
} else {
    // Loop to print the square
    for (let i = 0; i < size; i++) {
        console.log('X'.repeat(size));
    }
}
