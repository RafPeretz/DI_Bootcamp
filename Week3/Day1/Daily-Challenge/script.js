let planets = ["Mercure" ,"Venus", "Terre", "Mars", "Jupiter", "Saturne", "Uranus", "Neptune"]
function AddDivBetweenPlanet(argument) 
{
	let element = document.body;
	

	for (let i =0; i<planets.length ; i++)
	{
		let div = document.createElement("div");
		let section = document.createElement("section");


		div.textContent = planets[i];
		element.appendChild(div);
		element.appendChild(section)
		div.classList.add("planet");
		div.classList.add(planets[i]);


	}


}

AddDivBetweenPlanet();
