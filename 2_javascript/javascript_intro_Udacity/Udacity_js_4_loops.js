/*
 * Global scope. 
 * This variable declared outside of any function is called Global variable. 
 * Hence, you can use this anywhere in the code
 */
var opinion = "This nanodegree is amazing";

// Function scope
function showMessage() {
	// Local variable, visible within the function `showMessage`
	var message = "I am an Udacian!"; 
	
	// Block scope
	{
  		let greet = "How are you doing?";
		/*
		 * We have used the keyword `let` to declare a variable `greet` because variables declared with the `var` keyword can not have Block Scope. 
		 */
	} // block scope ends

    console.log( message ); // OK
    console.log( greet ); // ERROR. 
    // Variable greet can NOT be used outside the block

    console.log( opinion ); // OK	to use the gobal variable anywhere in the code

} // function scope ends 
 
 
 
 
 // 1.____________________________________________________________
var x = 1;
while (x <= 20) {
    if (x%3 === 0 && x%5 === 0){
        console.log("JuliaJames");
    }else if(x%3 === 0){
        console.log("Julia");
    }else if(x%5 === 0){
        console.log("James");
    }else{
        console.log(x);
    }
    x +=1;
}


 // 2.____________________________________________________________
var num = 99;
while (num > 0) {
    if(num >2){
        console.log(num+" bottles of juice on the wall! "+num+" bottles of juice! Take one down, pass it around... "+(num-1)+" bottles of juice on the wall!");
    }else if (num ===2){
        console.log(num+" bottles of juice on the wall! "+num+" bottles of juice! Take one down, pass it around... "+(num-1)+" bottle of juice on the wall!");
    }else{
        console.log(num+" bottle of juice on the wall! "+num+" bottle of juice! Take one down, pass it around... "+(num-1)+" bottles of juice on the wall!");
    }
    num-=1;
}


 // 3.____________________________________________________________
n = 60
while (n>=0){
    if (n===50){
        console.log("Orbiter transfers from ground to internal power");
    }
    else if(n===31){
        console.log("Ground launch sequencer is go for auto sequence start");
    }
    else if(n===16){
        console.log("Activate launch pad sound suppression system");
    }
    else if(n===10){
        console.log("Activate main engine hydrogen burnoff system");
    }
    else if(n===6){
        console.log("Main engine start");
    }
    else if(n===0){
        console.log("Solid rocket booster ignition and liftoff!");
    }else{
        console.log("T-"+n+" seconds");
    }
    n -=1;
}

// 4.____________________________________________________________
for (var x = 0; x < 5; x = x + 1) {
    for (var y = 0; y < 3; y = y + 1) {
      console.log(x + "," + y);
    }
  }
    // it's quite different from py
    // x++ or ++x // same as x = x + 1 
    // x-- or --x // same as x = x - 1
    // x += 3 // same as x = x + 3
    // x -= 6 // same as x = x - 6
    // x *= 2 // same as x = x*  2
    // x /= 5 // same as x = x / 5

// 5.____________________________________________________________
var x = 9;
while (x >= 1) {
    console.log("hello " + x);
    x = x - 1;
}
for (var x=9; x>=1; x--){
    console.log("hello " + x);
}

// 6.____________________________________________________________
var solution = 1;

for (let i = 1; i <= 12; i++) {
  solution *= i;
}
console.log(solution);


// 7.____________________________________________________________

for (var x=0; x<26; x++){
    for (var y=0; y<100; y++){
        console.log(x+"-"+y);
    }
}