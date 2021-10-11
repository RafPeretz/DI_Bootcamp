//Exercise 1 : Age Difference

let first = parseInt(prompt("enter the year he bord"));
let sec = parseInt(prompt("enter the year he bord"));

let between = 0;
if(first < sec)
{
	between = sec - first ; 
}
else
{
	between = sec - first ; 
}

console.log("in "+between+" year the younger will have the half of the older");

//Exercise 2 : Zip Codes

let zip = parseInt(prompt("enter the zip code"));

if(zip.length =! 5)
{
console.log("false")
}
else if(typeof zip != typeof 123 )
{
	console.log("false")
}
else
{
	console.log("true")
}

//Exercise 3 : Secret Word

let word = prompt('Please enter a word');
if (word.includes("a" || "e" || "i"|| "o"||"u" || "y"))
word = word.replace('a','1');
word = word.replace('e','2');
word = word.replace('i','3');
word = word.replace('o','4');
word = word.replace('u','5');
word = word.replace('y','6');

console.log(word);