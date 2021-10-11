//Exercise 1: Simple If/Else Statement

let x = 2;
let y = 4;

if (x>y)
console.log("x is the biggest number");

else if (x<y)
console.log("y is the biggest number");

else
console.log("The number are equals");

//Exercise 2: Chihuahua

let newDog = "Chihuahua";
if (newDog.length == 9)

console.log(newDog.length);
console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

if (newDog==="Chihuahua")
console.log("I love Chihuahuas, it’s my favorite dog breed");

else
console.log("I dont care, I prefer cats");



//Exercise 3: Even Or Odd

let numberUser = parseInt(prompt('Please insert a number'));

if (numberUser % 2 === 0) 

			console.log(numberUser,"is  an even number");

	else
			console.log(numberUser,"is  an odd  number");


//Exercise 4: Group Chat

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

if (users.length === 0)
console.log("no one is online");

if (users.length === 1)
	console.log(users[0] + "is online");

if (users.length === 2)
	console.log(users[0] +users[1]+ "is online");

if (users.length>2) {
	let otherUser = users.length -2;
	console.log(users[0] +users[1]+"and"+otherUser+ "more are online");
}




//if(users.length )