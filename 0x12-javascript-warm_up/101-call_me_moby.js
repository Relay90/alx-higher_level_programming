#!/usr/bin/node

// Function to execute another function x times
function callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
