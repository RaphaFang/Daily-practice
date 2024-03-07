"use strict";

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnsOpenModal = document.querySelectorAll(".show-modal");
const btnCloseModal = document.querySelector(".close-modal");
console.log(btnsOpenModal);

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

for (let i = 0; i < btnsOpenModal.length; i++) {
  btnsOpenModal[i].addEventListener("click", openModal);
}

btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

// you can check the key by doing this
// document.addEventListener("keydown", function (e) {
//   console.log(e.key);
// });

document.addEventListener("keydown", function (e) {
  console.log(e.key);

  if (e.key === "Escape") {
    closeModal();

    //   if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    //     closeModal();
    //   }
    //    I can't tell the different between two ways, but the 2nd actually more complite
  }
});
