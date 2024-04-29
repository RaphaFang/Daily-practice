// 90. js is a JIT language
// just in time compilation 一邊邊陳一邊執行

// beside global scope, all the scope are local
// scope chain
// one way only look "up"

// 94. hoisting，總之不要用 "var"，11:50 他只是一個byproduct
// TDZ, temporal dead zone, 暫時死區，JS讀變數，即便上方沒有會讀下方，如果有也會執行
"use strict";

// var variable is outside the current scope
// which is func. scope

// without use strict, the variable value would be given casually

const name = "Nick";
if (name === "Nick") {
  console.log(`j is named ${job}`);
  var job = "teacher";
}

// cus "undefined" is a false value, it could be set as a T/F condition
// if you declare the variable "after" the function, it could be alert

// this _________________________________________________
// 96.
// (06:13)
