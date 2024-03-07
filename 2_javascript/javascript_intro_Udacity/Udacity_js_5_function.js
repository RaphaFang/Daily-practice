  /*
Why use anonymous inline function expressions?
Using an anonymous inline function expression might seem like a very not-useful thing at first. 
Why define a function that can only be used once and you can't even call it by name?

Anonymous inline function expressions are often used with function callbacks that are probably not going to be reused elsewhere. 
Yes, you could store the function in a variable, give it a name, and pass it in like you saw in the examples above. 
However, when you know the function is not going to be reused, it could save you many lines of code to just define it inline.

  */


// // 1.____________________________________________________________
// AA = "";
// function laugh(num){
//     for(var a = 0; a<num; a++){
//         var lau = "ha";
//         AA += lau;
//     }
//     return AA+"!";
// }
// console.log(laugh(3));
// // 2.____________________________________________________________

// function prime(int){
//     for(var x=2; x<int; x++){
//         if (int%x ===0){
//             console.log(int+" divide by "+x);
//         }
//         return false;
//     }
// }
// prime(100);

// 3.____________________________________________________________
// Shadowing
// beawared, the local function would be rewrite if the global have the same name, without add var infront(means a nwe variable)

// function makeLine(length) {
//     var line = "";
//     for (var j = 1; j <= length; j++) {
//         line += "* ";
//     }
//     return line + "\n";
// }
function buildTriangle(length) {
    var triangle = "";
    var lineNumber = 1;
    for(lineNumber=1; lineNumber<=length; lineNumber++){
        triangle = triangle + makeLine(lineNumber);
    }
    return triangle;
}
console.log(buildTriangle(10));


// 4.____________________________________________________________
function makeLine(length) {
    var line = "";
    for (var j = 1; j <= length; j++) {
        line += "* ";
    }
    return line + "\n";
}

function buildTriangle(howbig){
    var A = "";       // be aware the variable in for loop, it'ii be rename each time.
    for(var step = 1; step <= howbig; step++){
        A = A + makeLine(step);
        }
    return A;
    }
console.log(buildTriangle(10));

// a way also work, but using consoal.log
// function makeLine(length) {
//     var line = "";
//     for (var j = 1; j <= length; j++) {
//         line += "* ";
//     }
//     return line + "\n";
// }

// function buildTriangle(howbig){
//     for(var step = 1; step <= howbig; step++){
//         console.log(makeLine(step));
//             }
//     }
// console.log(buildTriangle(10));


// 5.____________________________________________________________
var favoriteMovie = function displayFavorite(movieName) {    // the "displayFavorite" could be anonymous(super weired)
    console.log("My favorite movie is " + movieName);
  };
  function movies(messageFunction, name) {
    messageFunction(name);
  }
  movies(favoriteMovie, "Finding Nemo");
  // an anonymous to call a func.(super weired)

  function movies(messageFunction, name) {
    messageFunction(name);
  }
  movies(function displayFavorite(movieName) {
    console.log("My favorite movie is " + movieName);
  }, "Finding Nemo");
// an anonymous to call a func.(even weired...)


// 6.____________________________________________________________
function hahaFunc(num){      // name your func.
    var string = "";
    for (var x =1; x<=num; x++){
        string = string +"ha";
        }
    string = string+"!";
    return string;
}

function emotions(myString, myFunc) {
    console.log("I am " + myString + ", " + myFunc);
}
emotions("happy", hahaFunc(2));
// this would also work.
// in this way, there's no need for a inline func., but you need to name your func.
// at emotions(), all i need to do is indicating which func be called, and its input num.

function emotions(myString, myFunc) {
    console.log("I am " + myString + ", " + myFunc(2));
}

emotions("happy", function(num){
    var laugh = "";
    for (var x = 0; x<num; x++){
        laugh = laugh + "ha";
    }
    laugh = laugh + "!";
    return laugh;
}); 