"use strict";
// this 96._________________________________________________
// (4:00)
// 他提到，如果沒有用uss strict，this會叫道 windows，尤其在寫網頁的script
// (5:22)
// 如果用在Eventlistener，那麼這個this會是DOM

// this 97._________________________________________________
const calcAge = function (birthYear) {
  console.log(2037, -birthYear);
  console.log(this);
};
calcAge(1991);
const calcAgeArrow = (birthYear) => {
  console.log(2037 - birthYear);
  console.log(this);
};
calcAgeArrow(1980);
