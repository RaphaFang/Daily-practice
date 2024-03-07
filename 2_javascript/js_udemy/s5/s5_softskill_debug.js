"use strict";

const temperatures = [3, -2, -6, -1, "error", 9, 13, 17, 15, 14, 9, 5];
let highest = 0;
let lowest = 0;

for (let i = 0; i < temperatures.length; i++) {
  if (temperatures[i] > highest) {
    highest = temperatures[i];
  }
}
for (let i = 0; i < temperatures.length; i++) {
  if (temperatures[i] < lowest) {
    lowest = temperatures[i];
  }
}
console.log(highest, lowest);

// it works!!

const temp = function (tempinput) {
  let highest = tempinput[0];
  let lowest = tempinput[0];
  for (let i = 0; i < tempinput.length; i++) {
    if (tempinput[i] > highest) highest = tempinput[i];
  }
  for (let i = 0; i < tempinput.length; i++) {
    if (tempinput[i] < lowest) lowest = tempinput[i];
  }
  return `${highest}, ${lowest}`;
};
console.log(temp(temperatures));

// it works!!

// console.table(), give the table of all value of the object
