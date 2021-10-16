function playTheGame() 
{
	let num = 0 ;
	let computer=0;
	let response = confirm("Do you want to play the game ");
	if(response == false)
	{
		console.log("Ok no prob good bye");
	}
	else
	{
		computer = Math.round(Math.random()*10);
		test(num , computer);
	}
}
function test(userNumber,computerNumber){
	let count = 3 ;
	while(userNumber != computerNumber && count>0){
		if(count == 3 ){
			userNumber = chekNum();
		}else{
			userNumber = chekNum2();
		}
		if(userNumber == computerNumber){
			alert("WINNER");
		}else if(userNumber > computerNumber){
			alert("your num is bigger");
		}else{
			alert("your num is smaller");
		}
		count--;
		alert("you have just "+count+" more chance");
	}
	if(count == 0 ){
		alert("out of chances");
	}
}
function chekNum(){
	let num =prompt("Enter a num between 0 and 10 ");
	let bool = false;
	while(bool == false){
		if(isNaN(num)){
			console.log("Sorry Not a nuber");
			num =prompt("Retry to enter a num between 0 and 10 ");	
		}
		else{
			num = parseInt(num);
			if(num > 10 || num < 0 ){
				console.log("Sorry it’s not a good number");
				num =prompt("Retry to enter a num between 0 and 10 ");
			}else{
				console.log("that a good num ")	
				bool = true;
			}
		}
	}
	return num;
}
function chekNum2(){
	let num =prompt("Enter a new num between 0 and 10 because your was not the same as the computer");
	let bool = false;
	while(bool == false){
		if(isNaN(num)){
			alert("Sorry Not a nuber");
			num =alert("Retry to enter a num between 0 and 10 ");	
		}
		else{
			num = parseInt(num);
			if(num > 10 || num < 0 ){
				console.log("Sorry it’s not a good number");
				num =alert("Retry to enter a num between 0 and 10 ");
			}else{
				console.log("that a good num ")	
				bool = true;
			}
		}
	}
	return num;
}