let mov = document.getElementById("animate");
let btn = document.getElementsByTagName("button")[0];

btn.addEventListener("click",myMove);
function myMove(){
	let pos = 0;
	let id = setInterval(function() {
		if (pos == 350) {
			clearInterval(id);
		}
		else {
			pos++;
			
			mov.style.left = pos + "px";
		}
	}, 5);
}












