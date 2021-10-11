let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5
	},   
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2 
	}

};

// 1. Add the lastname Smith to the object

//userCart.lastName = "Smith";
userCart["lastName"] = "Smith";
console.log(userCart);

// 2. Change the price of the pear, so it will contain the Taxes. Taxes = 17%

//userCart["prices"]["pear"] = userCart["prices"]["pear"]*1.17;
userCart["prices"]["pear"] *= 1.17;

// 3. Ask the user for the fruit he wants between Apple, Banana and Pear. 
//Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA".

let userFruit = prompt('What do you want ?').toLowerCase();
console.log("the fruit user is ", userFruit);

//4. Console.log the price for the specific fruit the user wants

console.log(userCart["prices"][userFruit]);


//----------------------------------------------------------------------------------------


//Ex 1
//1. If the user is SignedIn - show him his name and password

if (userCart["isUserSignedIn"]===true)
{
	console.log(userCart["password"]);

}

//2. If not - alert the user "you need to sign in"

else 
	alert("you need to sign in");


//2nd exercise

//If the user is John AND his password is 1234 - alert him "You are signed in"

if (userCart["username"] === "John" && userCart["password"]===1234)
	alert("You are signed in");

// If the user is John OR his password is 1234 - alert him "One credential is false"
if (userCart["username"] === "John" || username["password"]===1234)
	alert("One credential is false");

else 
	alert("you need to sign in");


