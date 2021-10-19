// about the green box

// 1. Retrieve the green box
let item = document.getElementById("item");
let Seconditem = document.getElementById("itemSecond");

item.addEventListener("dragstart", startDragging);
Seconditem.addEventListener("dragstart", startDragging);

function startDragging (event) {
	console.log("start dragging", event.target.id);
	event.target.classList.add("startDragging");
	// console.log(event.dataTransfer)
	// syntax
	// event.dataTransfer.setData("type of data", id of the elem)
	event.dataTransfer.setData("text/plain",event.target.id)
}


// the black target boxes

let allDropZones = document.getElementsByClassName("dropzone");
console.log(allDropZones)

function addTheListeners (){
	for (let zone of allDropZones){
		zone.addEventListener("dragover", draggingOver)
		zone.addEventListener("drop", dropping)
	}
}

addTheListeners()

// create the dragging Over function
function draggingOver (event) {
	event.preventDefault();
	// console.log(event.target)
}



// Create the dropping function
function dropping(event){
    event.preventDefault();
	// console.log(event.target)
	// 1. retrieve the element that we want to srop
	let elementToDrop = event.dataTransfer.getData("text/plain")
	// 2. append the element on the drop zone
	let elemNode = document.getElementById(elementToDrop)
	event.target.appendChild(elemNode)
    elemNode.classList.add("newStyle");
    event.target.style.border = "5px dotted blue";
    
}

// 1. Change the style of the element when it's dropped in a valid drop zone
