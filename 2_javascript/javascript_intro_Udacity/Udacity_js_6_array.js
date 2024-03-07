// 1.____________________________________________________________
udaciFamily = ["Julia", "James", "nn" ];
for (var x=0; x<udaciFamily.length; x++){
    console.log(udaciFamily[x]);
}


// 2.____________________________________________________________
var captain = "Mal";
var second = "Zoe";
var pilot = "Wash";
var companion = "Inara";
var mercenary = "Jayne";
var mechanic = "Kaylee";

crew = [captain, second, pilot, companion, mercenary, mechanic];
for (var x=0; x<crew.length; x++){
    console.log(crew[x]);
}

// 3.____________________________________________________________
var donuts = ["glazed", "chocolate frosted", "Boston creme", "glazed cruller", "cinnamon sugar", "sprinkled"];
donuts.push("powdered"); // the `push()` method returns 7 because the `donuts` array now has 7 elements

var donuts = ["glazed", "chocolate frosted", "Boston creme", "glazed cruller", "cinnamon sugar", "sprinkled", "powdered"];
donuts.pop(); // the `pop()` method returns "powdered" because "powdered" was the last element on the end of `donuts` array


// 4.____________________________________________________________
var team = ["Oliver Wood", "Angelina Johnson", "Katie Bell", "Alicia Spinnet", "George Weasley", "Fred Weasley", "Harry Potter"];
console.log(hasEnoughPlayers(team));

function hasEnoughPlayers(player){
    if (player.len >6)
        return true;
    else
        return false;
}
console.log(hasEnoughPlayers(team));

// 5.____________________________________________________________
var reverseMe = ["h", "e", "l", "l", "o"];
reverseMe.reverse()

var turnMeIntoAString = ["U", "d", "a", "c", "i", "t", "y"];
turnMeIntoAString.join("")

words = ["cat", "in", "hat"];
words.toString()

// 6.____________________________________________________________
var test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4,
    19, 300, 3775, 299, 36, 209, 148, 169, 299,
    6, 109, 20, 58, 139, 59, 3, 1, 139
];

test.forEach(function(item, i){   // function(a,b) here,
    if(item%3 ===0){
        test[i] = test[i]+100;
        }
});
console.log(test);
// beaware that the func(a, b), you should not put named variable inside the ().
// instesd, put unnamed var


// 7.____________________________________________________________
var bills = [50.23, 19.12, 34.01,
    100.11, 12.15, 9.90, 29.11, 12.99,
    10.00, 99.22, 102.20, 100.10, 6.77, 2.22];

// way doesn't work
var totals = bills.map(function(bill, i){
    totals[i] = bill + bill*0.15;       //totals[i] here
    });
console.log(totals);
// can't use totals[i] here, it'll return "Cannot set properties of undefined (setting '0')"
// cuz, "totals" 's definition shouldn't contain itself. 

var totals = bills.map(function(bill, i){
    bill = bill*1.15;
    return Number(bill.toFixed(2));      // Number do the job of int() in py
});

console.log(totals);

// 8.____________________________________________________________
var numbers = [
    [243, 12, 23, 12, 45, 45, 78, 66, 223, 3],
    [34, 2, 1, 553, 23, 4, 66, 23, 4, 55],
    [67, 56, 45, 553, 44, 55, 5, 428, 452, 3],
    [12, 31, 55, 445, 79, 44, 674, 224, 4, 21],
    [4, 2, 3, 52, 13, 51, 44, 1, 67, 5],
    [5, 65, 4, 5, 5, 6, 5, 43, 23, 4424],
    [74, 532, 6, 7, 35, 17, 89, 43, 43, 66],
    [53, 6, 89, 10, 23, 52, 111, 44, 109, 80],
    [67, 6, 53, 537, 2, 168, 16, 2, 1, 8],
    [76, 7, 9, 6, 3, 73, 77, 100, 56, 100]
];

for (var x =0; x<10; x++){
    for(var y =0; y<10 ; y++){
        if (numbers[x][y]%2 ===0){
            numbers[x][y] = "even";
        }
        else{
        numbers[x][y] = "odd";}
    }
}
console.log(numbers);