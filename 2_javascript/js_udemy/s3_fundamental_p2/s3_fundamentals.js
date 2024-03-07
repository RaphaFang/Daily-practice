"use strict";

function logger(aaa, bbb) {
  let juice = `combine of ${aaa} and ${bbb}`;
  return juice;
}

console.log(logger("apple", "orange"));

// logger(10, 20);
// can't prompt func derectily, have to use console.log
// because ther's no "print()" inside the func(just like py's func)
// or name the func into a new variable.  e.g. let test = logger(10, 20)

// 3.4________________________________________________
// func declaration
function calcAge1(birthYear) {
  return 2037 - birthYear;
}
const age1 = calcAge1(1991);

// func expression
// be aware the expression produce values, the "calcAge2" hold the value
// expression might be more percise
const calcAge2 = function (birthYear) {
  return 2037 - birthYear;
};
const age2 = calcAge2(1991);

// 3.5________________________________________________
// Arrow func, arrow func won't get "this" key word

const calcAge = (birthYear) => 2037 - birthYear;
// no need to write the "return", if there is only 1 line

const yearUntilRetirement = (birthDay, firstName) => {
  const age = 2037 - birthDay;
  const retirement = 65 - age;
  return `S{firstName} retires in ${retirement} years`;
};

// 36________________________________________________
// func nest in another func

// 37________________________________________________
// return will exiect the func.
// command + D , will select all the same text

// 38________________________________________________
// ArrayName[index_number] = "replace_variable"
// you can put a func inside an array... mindblowing

// 40________________________________________________
// .push()    add at end
// .unshift() add at first

// .pop()     delete the last
// .shift()   delete the first

// .indexOf('the_element_like_to_search')
// if not include in the array, it return "-1"

// .includes('turn out the element inside the array or not')
// return true / false

// 42________________________________________________
// objects, the dict of js
const fang = {
  firstname: "Fang",
  lastname: "Rapha",
  age: 23,
  job: "jobless",
};
console.log(fang.firstname);
console.log(fang["firstname"]);

// would only work on bracket notation
const hi = "hi";
console.log(fang["firstname" + hi]);

// could also work with prompt, e.g.
const inputQ = prompt("chose a key");
if (fang[inputQ]) {
  console.log(fang[inputQ]); // no need for ''
} else {
  console.log("wrong request");
}

// add properties inside the object
fang.car = "scooter";
fang["facebook"] = "fangsihyu";

// 44. __________________________________
// we can add func in object, but only in expression

const fang = {
  firstname: "Fang",
  lastname: "Rapha",
  birthYear: 1991,
  job: "jobless",
  hasDriverLicense: true,

  // calcAge4: function (birthYear) {
  //   return 2037 - birthYear;
  // },

  // "this" in js(7:30)  前提是這個object內已經建立好‘birthYear’
  // 可以保持"dry"
  calcAge4: function () {
    return 2037 - this.birthYear;
  },

  // you could also create a new "key"
  calcAge5: function () {
    this.age = 2037 - this.birthYear;
    return this.age;
  },

  getSummary: function () {
    return `${this.firstname} is a ${this.calcAge5()}-year old ${
      this.job
    }, and he has ${this.hasDriverLicense ? "a" : "no"} driver license.`;
  },
};
console.log(fang.getSummary());
// it could work
console.log(fang.calcAge4(2000));
console.log(fang["calcAge4"](2000));

// for "this" func, you have to make sure who calls the func?
// in this case, "fang" calls the function
console.log(fang.calcAge5());

// 46.________________________________________________
// for loop
for (let rep = 1; rep <= 10; rep++) {
  console.log(rep);
}
// 47.________________________________________________
const newArray = ["Rapha", "Fang", 2024 - 2000, "jobless", ["a", "b", "c"]];
// "continue" (17:00)
// "break" (21:00)

// 48.________________________________________________
// reverse Loop
for (let i = newArray.length - 1; i <= 0; i--) {
  console.log(i, newArray[i]);
}
// loop inside loop

// 49.________________________________________________
let rep = 0;
while (rep <= 10) {
  console.log(rep);
  rep += 1;
}

let dice = 0;

while (dice !== 6) {
  console.log(`You rolled a ${dice}`);
  dice = Math.trunc(Math.random() * 6) + 1;
  if (dice === 6) {
    console.log("Loop is ending...");
  }
}
