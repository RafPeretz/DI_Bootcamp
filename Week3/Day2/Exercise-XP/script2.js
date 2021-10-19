let button = document.getElementById("submit");

button.addEventListener("click",function(event){
	event.preventDefault();
	let radius = document.getElementById("radius").value;
	let volume = document.getElementById("volume");

	let sum = (4/3)* Math.PI * Math.pow(radius, 3);

	console.log('Volume of Sphere: '+sum.toFixed(2));

	volume.value= sum;
})
