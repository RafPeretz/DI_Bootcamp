//Exercise 1 : Change The Navbar

document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation");

let ul = document.getElementById("list");
let li = document.createElement("li");
li.appendChild(document.createTextNode("Logout"));

ul.appendChild(li);




	