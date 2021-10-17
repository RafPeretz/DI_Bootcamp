let divelement = document.getElementById("container");
let divSecondelement = document.getElementsByTagName("div")[0];

let ulSecondElement = document.getElementsByClassName("list") ;
let  ulElement = document.getElementsByTagName("ul");

let ilElement = document.getElementsByTagName("li")[0];

for (let ul of ulElement)
{
	console.log(ul.children[0].textContent, ul.children[1].textContent)
}
console.log(ilElement);

// 1. Create a function that adds the name of each students to 
// a paragraph
// 2. each paragraph needs to be background yellow, font-size 25px
// 3. Add the 3 paragraph to the div already on the page






let names = ["John", "Lola", "Tom"];

for (let i =0; i<names.length ; i++)
{
	let para = document.createElement("p");
	let node = document.createTextNode(names[i]);
	para.appendChild(node);

	let element = document.getElementById("container");
	element.appendChild(para);



}
for(let j = 0 ; j < 3 ; j++)
{
	element.children[j].setAttribute("class", "para2");
}





