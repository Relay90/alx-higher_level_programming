#!/usr/bin/node

// Script: 3-value_argument.js

// Get the first argument from process.argv
const firstArgument = process.argv[2];

// Check if the first argument exists and print the appropriate message
if (!firstArgument) {
    console.log("No argument");
} else {
    console.log(firstArgument);
}
