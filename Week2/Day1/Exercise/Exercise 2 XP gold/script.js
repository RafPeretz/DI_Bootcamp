//exercise 1 

let me = ["my","favorite","color","is","blue"]

let sentence = `${me[0]} ${me[1]} ${me[2]} ${me[3]} ${me[4]} `

console.log(sentence);


//exercise 2

let str1 = "raf" ;
let str2 = "sam";
let str3 = str2 + " " + str1;
console.log(str3)
let char1 = str1.substr(2);
let char2 = str2.substr(2);
str1 = str1.replace(char1 ,char2 );
str2 = str2.replace(char2,char1 );
str3 = str2 + " " + str1;
console.log(str3)


//exercise 3

let num1 = parseInt(prompt('Please insert a number'));
let num2 = parseInt(prompt('Please insert a second number'));
let sum = num1 + num2;

console.log(sum);
 



 	