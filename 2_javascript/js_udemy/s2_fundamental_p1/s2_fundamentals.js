// // alert("Hello world!");
// let js = "amazing";
// if (js === "amazing") alert("ssss");
// console.log(js);
// console.log(20 + 1);
// 1. __________________________________________________
// console.log(typeof 0);
// console.log(typeof null);

// 2. __________________________________________________
// avoid using "var"
// "const" can't declare empty, or be redefined.
// avoid call the variable directily, e.g.: firstName = "Fang";
// because, it would be a global variable.

// 3. __________________________________________________
// x**2 = x*x
// it's fine to prompt like this:
// console.log(a - b > c - d);           it'll function like human process
/* Write your code below. Good luck! 🙂 */
// let massMark, heightMark, massJohn, heightJohn, BMIMark, BMIJohn;
// massMark = 78;
// heightMark = 1.69;
// massJohn = 92;
// heightJohn = 1.95;
// BMIMark = massMark / (heightMark * heightMark);
// BMIJohn = massJohn / (heightJohn * heightJohn);

// console.log(BMIMark, BMIJohn);

// let markHigherBMI = BMIMark > BMIJohn;
// console.log(markHigherBMI);

// 4. __________________________________________________
// the print(f""") in js.
// let myName = "Rapha";
// let birthDay = 23;
// let string = `I'm ${myName}, I'm ${birthDay} old.`;
// console.log(string);

console.log("a b c \n ab");
// or using ``,
console.log(`a
b
c`);

// 5. __________________________________________________
// still have the local global distinguish

// 6.--------------------------------------------------------------------
const massMark = 78;
const heightMark = 1.69;
const massJohn = 92;
const heightJohn = 1.95;

const BMIMark = massMark / (heightMark * heightMark);
const BMIJohn = massJohn / (heightJohn * heightJohn);
console.log(BMIMark, BMIJohn);

if (BMIMark > BMIJohn) {
  console.log(`Mark's BMI (${BMIMark}) is higher than John's (${BMIJohn})!`);
} else {
  console.log(`John's BMI (${BMIJohn}) is higher than Mark's (${BMIMark})!`);
}

// 7.--------------------------------------------------------------------
//  Number()
// String()

// 8.--------------------------------------------------------------------
// five false value, 0 / '' / undefined / null / NaN
// 9.--------------------------------------------------------------------
prompt("what's your favourate");

// 10.--------------------------------------------------------------------
// && and
// || or
// ! not

// 11.--------------------------------------------------------------------
let scoreDolphins = (97 + 112 + 101) / 3;
let scoreKoalas = (109 + 95 + 106) / 3;

if (scoreDolphins > scoreKoalas) {
  console.log("Dolphins win the trophy");
} else if (scoreKoalas > scoreDolphins) {
  console.log("Koalas win the trophy");
} else {
  console.log("Both win!");
}

// 12.--------------------------------------------------------------------
// switch(){}
const day = "monday";
switch (day) {
  case "monady":
    console.log("today is monday");
}
// 13.--------------------------------------------------------------------
const bill = 275;
let tip = bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
console.log(
  `The bill was ${bill}, the tip was ${tip}, and the total value ${bill + tip}.`
);
