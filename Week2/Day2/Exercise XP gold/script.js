// Exercise 1 : The World Translator

 let lang = prompt("wich lag you speak");

lang = lang.toLowerCase()
;
switch(lang) {

	case "french":
	console.log("french")
	break;

	case "english":
	console.log("english")
	break;

	case "hebreu":
	console.log("hebreu")
	break;
	
	default:
	console.log("01110011 01101111 01110010 01110010 01111001")

}


//Exercise 2 : The Grade Assigner

let grade = parseInt(prompt('Please enter your grade'));

if (grade>90)
console.log("A");

if (grade > 80 && grade < 90)
console.log("B");

else if (grade > 70 && grade < 80)
console.log("C");

 else if (grade < 70)
console.log("D");

// Exercise 3 : Verbing

let verb = prompt('Please enter a verb');
let last3 = verb.slice(-3);


if (verb.length >= 3 && last3 != "ing"){
verb += "ing";
console.log(verb);}

 if (verb.length >= 3 && last3 == "ing"){
verb += "ly";
console.log(verb);
}

if (verb.length < 3)
	console.log(verb);






