//Exercise 1 : Your Favorite Colors

let colors = ["Blue","Yellow","Green","Red","Pink"];

for (let i =0 ;i<=colors.length -1;i++)
{
	console.log( "My #" + (i+1) + " choice is " + colors[i]);
}

//Exercise 2 : List Of People

let people = ["Greg", "Mary", "Devon", "James"]
people.shift();
console.log(people);

people.pop();
people.push("Jason");
console.log(people);

people.push("Rafael");
console.log(people);

for (let i =0; i<=people.length -1; i++)
{
  console.log(people[i]);
}

let peopleCopy = people.slice(1);
console.log(peopleCopy);

console.log(people.indexOf("Mary"));

console.log(people.indexOf("Foo"));

let last = "Samuel"
people.push(last);
console.log(people);

//Exercise 4 : Attendance

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let name = prompt('Please enter your name: ');

for (let key in guestList)
{
	if(key===name)
	{
		console.log("Hi! I'm " +name+ " and I'm from "+ guestList[key]);
	}
	else console.log("Not in the list");

}

//Exercise 5 : Family

let family = {
  LastName: "Peretz",
  Member: 4,
  hasADog: true
}

for(let key in family)
{
console.log(key);
console.log(family[key]);
}

//Exercise 6 

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

let sentence ="";
for(let key in details)
{
	sentence += " " + key;
 	sentence += " " +details[key];
}
console.log(sentence)

//Exercise 7 : Secret Group

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
names = names.sort();

let societyName = " ";

for (let i =0 ;i<=names.length -1;i++)
{
societyName += names[i].charAt(0);
}

console.log(societyName);