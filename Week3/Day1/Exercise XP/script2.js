//Exercise 2 : Users

for (let i = 0; i<2; i++)
{
	ul = document.getElementsByTagName("ul")[i];
	ul.children[0].textContent= "Rafael"
}

let parentUl = document.getElementsByTagName("ul")[1];
let childUl = parentUl.children[1];
parentUl.removeChild(childUl);
