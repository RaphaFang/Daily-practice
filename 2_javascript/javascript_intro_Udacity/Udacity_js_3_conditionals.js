// the Boolean value false
// the null type
// the undefined type
// the number 0
// the empty string ""
// the odd value NaN (stands for "not a number"

// 1.____________________________________________________________
var number = 700;
if (number%2 === 0) {
    console.log("even");
} else {
    console.log("odd");
}


// 2.____________________________________________________________
var musicians = 4.5;
if (musicians <= 0) {
    console.log("not a group");
}else if (musicians === 1){
    console.log("solo");
}else if (musicians === 2){
    console.log("duet");
}else if (musicians === 3){
    console.log("trio");
}else if (musicians === 4){
    console.log("quartet");
}else (musicians > 4);{
    console.log("this is a large group");
}
// else if (musicians === 4){
//     console.log("quartet");       ; is at the end
// should prompt ";" at the last line of elseif function.


// 3.____________________________________________________________
// && conjunction 
// || disjunction
// !  nigation
var flavor = "chocolate";
var vessel = "cone";
var toppings = "sprinkles";
var f1 = false; var v1 = false; var t1 = false;

if (flavor === "vanilla" || flavor === "chocolate"){
    f1 = true;
}    
if (vessel === "cone" || vessel ==="bowl"){
    v1 = true;
}
if (toppings === "sprinkles" || toppings === "peanuts"){
    t1 = true;
}
if (f1 && v1 && t1 === true){
    console.log(`I'd like two scoops of ${flavor} ice cream in a${vessel} with ${toppings}.`);
}

// or a more simple way...
var flavor = "strawberry";
var vessel = "cone";
var toppings = "cookies";

if ((flavor === "vanilla" || flavor === "chocolate") && (vessel === "cone" || vessel === "bowl") && (toppings === "sprinkles" || toppings === "peanuts")){
        console.log ("I'd like two scoops of " + flavor + "ice cream in a " + vessel + "with " + toppings + ".")
}


// 4.____________________________________________________________
// js can't do A<B<C, it could only do A<B && B<C
var shirtWidth = 21;
var shirtLength = 99;
var shirtSleeve = 8.40;
var size = "AAA";

if ((shirtWidth>=18 && shirtWidth<20) && (shirtLength>=28 && shirtLength<29) && (shirtSleeve>=8.13 && shirtSleeve<8.38) ) {
    size = "S";
}else if ((shirtWidth>=20 && shirtWidth<22) && (shirtLength>=29 && shirtLength<30) && (shirtSleeve>=8.38 && shirtSleeve<8.63) ) {
    size = "M";
}else if ((shirtWidth>=22 && shirtWidth<24) && (shirtLength>=30 && shirtLength<31) && (shirtSleeve>=8.63 && shirtSleeve<8.88) ) {
    size = "L";
}else if ((shirtWidth>=24 && shirtWidth<26) && (shirtLength>=31 && shirtLength<33) && (shirtSleeve>=8.88 && shirtSleeve<9.63) ) {
    size = "XL";
}else if ((shirtWidth>=26 && shirtWidth<28) && (shirtLength>=33 && shirtLength<34) && (shirtSleeve>=9.63 && shirtSleeve<10.13) ) {
    size = "2XL";
}else if ((shirtWidth>=28) && (shirtLength>=34) && (shirtSleeve>=10.13) ) {
    size = "3XL";
}
console.log(size);

// 5.____________________________________________________________
// my week part, need more practice...
// the second way work the same, but more prolix.
var eatsPlants = false;
var eatsAnimals = true;
var category = eatsPlants ? (eatsAnimals ? "omnivore" : "herbivore") : (eatsAnimals ? "carnivore" : "undefined");
console.log(category);

if (eatsPlants == 1){
    if (eatsAnimals == 1){
        category =  "omnivore";
    }else{
        category = "herbivore";
    }
}else{
    if (eatsAnimals ==1){
        category = "carnivore";
    }else{
        category = "undefined";
    }
}
console.log(category);

// 6.____________________________________________________________
var education = 'no high school diploma';
var salary = 0;

switch (education){
case 'no high school diploma':
    salary = 25636;
    break;
case 'a high school diploma':
    salary = 35256;
    break;
case 'an Associate\'s degree':
    salary = 41496;
    break;
case 'a Bachelor\'s degree':
    salary = 59124;
    break;
case 'a Master\'s degree':
    salary = 69732;
    break;
case 'a Professional degree':
    salary = 89960;
    break;
case 'a Doctoral degree':
    salary = 84396;}

console.log("In 2015, a person with " + education + " earned an average of $" + salary.toLocaleString("en-US") + "/year.");
