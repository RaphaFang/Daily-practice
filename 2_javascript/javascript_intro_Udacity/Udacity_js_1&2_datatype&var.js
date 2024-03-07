// single double quote, work the same
// "\t" = tab
// "\\" = \ (backslash), if you want to generate \\, you have to code "\\\\"

// 1.____________________________________________________________
console.log("hiya friend!")


// 2.____________________________________________________________
// F = C x 1.8 + 32
var celsius = 12;
var fahrenheit = celsius*1.8 + 32;
console.log(fahrenheit);


// 3.____________________________________________________________
// we can count the number of a str, (but i wonder where do i need this?)
var a = Boolean("green"> "blue")
console.log(a);

// 4.____________________________________________________________
// Programming Quiz: Favorite Food (2-3)
console.log("My favorite food is lemon tart");

// 5.____________________________________________________________

var joke = ("Why couldn't the shoes go out and play?\nThey were all \"tied\" up!");
console.log(joke);

// 6.____________________________________________________________
var haiku = ("Blowing from the west \nFallen leaves gather \nIn the east.");
console.log(haiku);

// 7.____________________________________________________________
// var x = null; means x is a var, but it's value haven't be define.
// ' ' == false, Returns: true. Both the operands on either side of the == operator are first converted to zero, before comparison.
// If we don't want to convert the operands, before comparison, we have to use a strict comparison ===, that is explained below.
// "Hello" % 10 = Number("Hello"), Returns: NaN, When "Hello" is converted into a number, the result is NaN(Not a Number). Therefore, the result of the operation is also NaN.
// "3" > 1, true >= 0, 1 !== false, 3 === 3 is "true" ... such a slopy language


// 8.____________________________________________________________
var bill = 10.25 + 3.99 + 7.15;
var tip = 0.15 * bill;
var total = bill + tip;
console.log(tip);
console.log("$"+total);
// truly a slopy language, 0.15*bill = float with 4 decimal, but 1.15*bill = will get more decimal...


// 9.____________________________________________________________
 var firstName = ("Fang");
 var interest =("make my mony worth");
 var hobby=("put my interest into practice");
 var awesomeMessage =("Hi, my name is " +firstName+". I love "+interest+". In my spare time, I like to "+hobby+".");
 console.log(awesomeMessage);
 // ";" , don't forgot