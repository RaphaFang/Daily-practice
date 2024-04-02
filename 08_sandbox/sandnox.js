// "use strict";
function printVariable() {
  var variable = 1;
  console.log(`printG: `, variable);
}

printG();
console.log(`Global G:`, g);

("use strict");
function printVariable() {
  console.log(`Func V: `, v);
  let v = 1;
}

console.log(`Global V:`, v);
printVariable();

//___________________

// function printV1() {
//   var v = 2;
//   console.log(`printV1:`, v);
// }
// let v = 10;
// printV1(); // => pritnV1: 2
// try {
//   console.log(v); // error
// } catch {
//   console.log("not find v");
// }

// _________________

// function printL1() {
//   let l = 3;
//   console.log(`printL1:`, l);
// }

// printL1(); // => printL1: 3
// try {
//   console.log(`Global l:`, l); //error
// } catch {
//   console.log(`not find l`);
// }

// _________________

// function printL3() {
//   if (true) {
//     let l = 3;
//   }

//   try {
//     console.log(`printL2:`, l);
//   } catch {
//     console.log(`can't find l in printL3`);
//   }
// }
// printL3(); // => can't find l in printL2

// _______________

// function printL2() {
//   console.log(l);
//   let l = 3;
// }

// try {
//   printL2();
// } catch {
//   console.log(`can't find l in printL2`);
// }

// _______________
// 'use strict';
// do
//     local v = 1
//     do
//         local v = v + 1
//         print(v) // 2
//     end
//     print(v) // 1
// end

// ("use strict");

("use strict");
function printG() {
  console.log(`printG: `, g);
  let g = 1;
}
// let g = 10;

printG(); // => printG: 1
console.log(`Global G:`, g); // => Global G: 1
