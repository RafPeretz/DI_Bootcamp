let listTasks = [];

let button = document.getElementsByTagName("button")[0];

button.addEventListener("click", function ()
{
	event.preventDefault();
	let input = document.getElementById("input").value;
	console.log(input)
	if(input =="")
	{
		
		alert("Please enter a stack to do");
	}

	else 
	{
		console.log("john");

		listTasks.push(input);
		let p = document.createElement("p");
		let hr = document.createElement("hr");
		let secondInput = document.createElement("input")

		let div = document.getElementsByClassName("listTasks")[0];
		p.appendChild(document.createTextNode(input));
		secondInput.setAttribute("type","checkbox")
		div.appendChild(p);
		p.appendChild(hr);
		p.appendChild(secondInput);




	}
	console.log("john");
})
