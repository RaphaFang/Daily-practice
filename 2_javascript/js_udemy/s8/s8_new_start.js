"use strict";
// this 96._________________________________________________
// (4:00)
// 他提到，如果沒有用uss strict，this會叫道 windows，尤其在寫網頁的script
// (5:22)
// 如果用在Eventlistener，那麼這個this會是DOM

// !this 97._________________________________________________
console.log(this);
// 會是window object
// Window {parent: Window, opener: null, top: Window, length: 0, frames: Window, -}

const calcAge = function (birthYear) {
  console.log(2037, -birthYear);
  console.log(this);
};
calcAge(1991);
// 在"use strict"; 會是undefined

const calcAgeArrow = (birthYear) => {
  console.log(2037 - birthYear);
  console.log(this);
};
calcAgeArrow(1980);
// 會是window object，因為 => arror func 沒有自己的 this keyword
// 所以會只射到lexical this keyword，也就是 parent func 得出來
// Window {parent: Window, opener: null, top: Window, length: 0, frames: Window, -}

const jonas = {
  year: 1991,
  calcAge: function () {
    console.log(year - jonas.this);
  },
};
jonas.calcAge();
// 這邊的this會是 jonas 這個dict {year:1991,calcAge:f }
// 但是，為甚麼this會是jonas，事因為jonas是『最靠近這個func的object』
// 證明這點，透過以下
const matilda = {
  year: 2017,
};
matilda.calcAge = jonas.calcAge;
matilda.calcAge();
// 這邊的this會是 matilda 這個dict {year:2017,calcAge:f }
// 但是，為甚麼this會是matilda，事因為matilda是『最靠近這個func的object』

// !this 98._________________________________________________
var firstName = "Matilda";
const jonas_2 = {
  firstName: "Jonas",
  year: 1991,
  calcAge: function () {
    console.log(this);
    console.log(2037 - this.year);
  },
  greet: () => console.log(`Hey ${this.firstName}`),
};
jonas_2.greet();
// => func, 沒有this key, 所以他會找 global 的變數當作this
// 如果用的是 var，就會變成全域變數
// 也就是吃到 var firstName = "Matilda"; 這會是global object
// 所以不要使用var，隨便變成全域變數太危險

// 如果不用 var firstName = "Matilda";
// 這邊較this，就會變成 undefined，因為上邊這些都只是宣告，並不是物件，叫物件的函數，前方沒有最靠近的object
// 所以會是undefined
