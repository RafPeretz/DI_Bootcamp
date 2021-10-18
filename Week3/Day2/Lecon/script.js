let button = document.getElementById("btn");
let title = document.getElementById("title")

let redButton = document.getElementById("red");
let blueButton = document.getElementById("blue");


redButton.addEventListener("click", function ()
{
	document.body.style.backgroundColor = "red";
})

blueButton.addEventListener("click", function ()
{
	document.body.style.backgroundColor = "blue";
})


// SYNTAX:
// element.addEventListener(DOM events, callback function);

// with a function as a callback function
// function welcome(){
// 	console.log("hello")
// }

// button.addEventListener("click", welcome)

// title.addEventListener("click", welcome)


// // with anonymous function as a callback function
// button.addEventListener("click", function (){
// 	console.log("hello")
// })

// button.addEventListener("mouseover", function (){
// 	console.log("hovered")
// })

// title.addEventListener("click", function (){
// 	console.log("hello")
// })

// 1. Add inside the HTMl file a div of id container (do it directly in the HTML)
// 2. Add one button per color inside the div container (do it directly in the JS)
// 3. Each button should have an "click" event listener that 
// changes the background color of the document,  to the color of the button (do it directly in the JS)

// Example:
// when you click on the YELLOW button, it should change the document 
// background color to yellow

let colors = ["blue", "yellow", "green", "pink"];

// let blueButton = document.createElement("btn");
// let yellowButton = document.createElement("btn");
// let greenButton = document.createElement("btn");
// let pinkButton = document.createElement("btn");


for (let i=0 ;i<colors.length; i++) 
{
	let nameButton = colors[i];
	let button = document.createElement("button");
	let div = document.getElementById("container");
	button.appendChild(document.createTextNode(nameButton));

	div.appendChild(button);

	button.addEventListener("click", function ()
	{
		document.body.style.backgroundColor = nameButton;
	})


}



// Exercise:

let pics = [
"https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
"https://images.pexels.com/photos/2253275/pexels-photo-2253275.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
"https://images.pexels.com/photos/3439576/pexels-photo-3439576.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
]

// 1. Using this array, create a button on the page that when clicked on 
// display one animal randomly




let button = document.body.createElement("button");
let div = document.getElementById("buttonpic");
button.appendChild(document.createTextNode("Click me !"));
div.appendChild(button);

button.addEventListener("click", function ()
{
	document.body.style.backgroundImage= pics[math.floor(math.random*pics.length)];
})



// 2. Set a class to the image, so each image will be 200px height, and width, and in the middle of the page
// 3. Add a button next to each image
// 4. When we click on one image, it should disapear(ie. be deleted),
// When we hover on the image, it should display the "alt".


	// let div = document.createElement("div");

	// div.setAttribute(‘id’,‘container’);
