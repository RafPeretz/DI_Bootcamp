//Exercise 1 : Change The Article
//1. Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
let article = document.getElementsByTagName("article")[0];
article.lastElementChild.remove();


//2.Add an event listener which will change the background color
// of the h2 tag from the DOM when clicked on.

let h2 = document.getElementsByTagName("h2")[0];
h2.addEventListener("click", function ()
{
	h2.style.backgroundColor = "blue";
})

// 3. Set the font size of the h1 tag to a random pixel size between 0 to 100.

let h1 = document.getElementsByTagName("h1")[0];

h1.addEventListener("click", function ()
{
	h1.style.fontSize = Math.floor(Math.random() * 100)+"px";
})


// 4. Add an event listener which will hide the h3 when it’s clicked on (use the display property).

let h3 = document.getElementsByTagName("h3")[0];

h3.addEventListener("click", function ()
{
	h3.style.display = "none";

})

// 5. Add a <button> to the HTML file, that when clicked on, 
//should make the text of all the paragraphs, bold.

let button = document.getElementsByTagName("button")[0];
button.addEventListener("click", function ()
{
	article.style.fontWeight = "bold";

}) 

let btn2 = document.getElementById("submit");


btn2.addEventListener("click",function(event){
	event.preventDefault();
	let Fname = document.getElementById("fname");
	let Sname = document.getElementById("lname");
	let FnameValue = Fname.value;
	let SnameValue = Sname.value;
	if(FnameValue != ""){
		let p = document.createElement("p");
		p.textContent= FnameValue+" "+SnameValue;
		let div = document.getElementsByClassName("usersAnswer")[0];
		div.appendChild(p);
	}
})


let secondPara = document.getElementsByTagName("p")[1];

secondPara.addEventListener("mouseover", function (){
	secondPara.style.opacity = "0.5";
})
console.log(secondPara);

