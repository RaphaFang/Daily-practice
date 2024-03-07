// "typeof", work the same as type() in py
// don't name the key of dictionary like "1name" or "name-me"

// 1.____________________________________________________________

var facebookProfile ={
    name: "Rapha",
    friends: 10,
    messages:["AAA"],
    postMessage: function postMessage(){
        facebookProfile.messages.push("new message");   // whatout here
    },
    deleteMessage: function deleteMessage(index){
        facebookProfile.messages.splice(index, 1 );      // remove the actual index, is no need for the third prompt at(index, 1, "")
    },
    addFriend : function addFriend(){
        facebookProfile.friends += 1;
    },
    removeFriend : function removeFriend(){
        facebookProfile.friends -= 1;
    },
};

// beaware that if you want to call use the variable in "object",
// you have to call the var like this, "facebookProfile.messages.push("new message");"
// not "messages.push("new message");"


// 2.____________________________________________________________
var donuts = [
    { type: "Jelly", cost: 1.22 },
    { type: "Chocolate", cost: 2.45 },
    { type: "Cider", cost: 1.59 },
    { type: "Boston Cream", cost: 5.99 }
];
donuts.forEach(function(item){
    console.log(item.type+" donuts cost $"+item.cost+" each");
});
// (1.) stander answer


donuts.forEach(function(i){
    console.log(i.type + " donuts cost $" + i.cost + " each");
});
// (2.) my answer


donuts.forEach(function(i){
    console.log(donuts[Number(i)].type + " donuts  cost $" + donuts[i].cost + " each");
});
// (3.) incorrect

/* 
donuts.forEach(function(donut){}, 
是直接將donuts[]，當作loop的單位，donuts內部的資料數量為開始、停止的條件
        而不是說，在function()，依據我胃進去某個陣列運作
*/

/*
在(3.)，i 會是依據donuts[]的第一筆資料匯入，也就是element，
並非代數（1 2 3 ...），若要設定代數，要到function(a,b,c,)的 b 空位才可以命令。
因此，沒辦法透過 donuts[i] 叫出陣烈的第1筆資料
*/

