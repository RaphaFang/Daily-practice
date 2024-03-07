"use strict";

document.querySelector(".message").textContent = "web reset";
document.querySelector(".score").textContent = 0;
document.querySelector(".guess").value = 0;

// this works, but try below
// document.querySelector(".check").addEventListener("click", function () {
//   console.log(typeof document.querySelector(".guess").value);
// });
// this works, but try below

// Math.random(), gives you a float between 0~1
// as a result, you have to multiple the Math.random() and +1
// use trunk() to remove the float

let score = 20;
let secretNumber = Math.trunc(Math.random() * 20) + 1;
let highscore = 0;
// key : 記得把要變動、多次定義的數字變成 "let" not "const"

// display random code of box
// document.querySelector(".number").textContent = secretNumber;

const displayMessage = function (message) {
  document.querySelector(".message").textContent = message;
};

document.querySelector(".check").addEventListener("click", function () {
  const guess = Number(document.querySelector(".guess").value);
  if (!guess) {
    displayMessage("noooo number!");
  } else if (guess === secretNumber) {
    displayMessage("Correct Number!!");
    document.querySelector("body").style.backgroundColor = "#60b347";
    document.querySelector(".number").style.width = "30rem";
    if (score > highscore) {
      highscore = score;
      document.querySelector(".highscore").textContent = score;
    }
  } else if (guess !== secretNumber) {
    if (score > 1) {
      displayMessage(guess > secretNumber ? "too high" : "too low");
      score--;
      document.querySelector(".score").textContent = score;
    } else {
      displayMessage("You loss the game.");
      document.querySelector(".score").textContent = 0;
    }
  }
});

document.querySelector(".again").addEventListener("click", function () {
  score = 20;
  secretNumber = Math.trunc(Math.random() * 20) + 1;
  document.querySelector(".number").textContent = secretNumber;
  document.querySelector("body").style.backgroundColor = "#222";
  displayMessage("New Game Start");
  // be aware that, to give the value of the variable, just write "score = 20; "
  // no need to declare once
  document.querySelector(".score").textContent = score;
  document.querySelector(".guess").value = "";
  document.querySelector(".number").style.width = "15rem";
});
