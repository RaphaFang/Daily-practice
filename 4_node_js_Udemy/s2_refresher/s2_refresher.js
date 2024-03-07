"use strict";
// var name = "nick";

// console.log();
// 1.--------------------------------------------------------------------

// if you name a var in "let", the first value won't be change ????
// but if you name a var in "const", beside it won;t be change, it gives "error"

// 2.--------------------------------------------------------------------
// named func.
// anonymous func.
// const aaa = (xx, yy, zz) =>{return(...)}
// const bbb = (xx, yy) => xx+ yy;
// ther's no need to write "return" in short-hand

// 3.--------------------------------------------------------------------
// S2.15. working with objects, properties & methods
// class & function inside dict.
//
// const person = {
//   name: "Rapha",
//   age: 23,
//   greet: () => {
//     console.log("Hi, I am " + this.name);
//   },
// };
// person.greet();
//  the "this.name" would display "undefined"
// to resolved this, use old school way func.
// const person = {
//   name: "Nick",
//   age: 23,
//   greet: function () {
//     console.log("Hi, I am " + this.name);
//   },
// };
// person.greet();
// or
// const person = {
//   name: "Nick",
//   age: 23,
//   greet() {
//     console.log("Hi, I am " + this.name);
//   },
// };
// person.greet();

// 4.   .map()--------------------------------------------------------------------
// // const person = { name: "Rapha", age: 23 };
// const hobbies = ["sport", "cooking"];
// console.log(hobbies.map((hobby) => "Hobby: " + hobby));
// // console.log(hobbies.map(  "you should always put a function inside .map()");
// // beside, the map() won't add item into the existing array.
// console.log(hobbies);

// // 5. S2._18
// // .slice() /  [...hobbies]  / {...person}  / (...args)--------------------------------------------------------------------
// const copiedArray = hobbies.slice;
// const secondCopieedArray = [...hobbies];
// const copiedPerson = { ...person };
// // which could also used on dict.
// const toArray = (...args) => {
//   // name of the func & it's input(...args)
//   return args;
//   // actual item to put in a list
// };
// console.log(toArray(1, 2, 3, 4));

// 6. S2.19--------------------------------------------------------------------
const person = { name: "Rapha", age: 23 };

// const printName = (personData) => {
//   console.log(personData.name);
// };

const printName = ({ name, age }) => {
  console.log(name, age);
};
printName(person);

const { name, age } = person;
console.log(name, age);

// the three work the same

// 6. S2.19--------------------------------------------------------------------
const fetchData = (callback) => {
  setTimeout(() => [], 1500);
};
// 真的看不懂....先把js知識補起來
