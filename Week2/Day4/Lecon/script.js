// I want to go through the colors array, and print each letter of each color 

let colors = ["blue", "red", "yellow", "lightblue"];

for (let i = 0; i <colors.length; i++)
 {
    console.log("index :" , i);
    console.log("colors" , colors[i]);
    console.log("colors length", colors[i].length);

 	for (let j = 0; j <colors[i].length; j++) 
 	{
 	  console.log(colors[i][j]);	
 	}
 }
	// /1st function
//1. Create a function, that accepts 3 arguments:
//* name of pet
//* color of pet
//  breed of pet

function Foo(namePet , colorPet , breedPet)
{
    alert(namePet ,colorPet , breedPet);
}

// 2nd function 

function Foo2 (age , arrColor)
{
    let twiceMyage = age *2 ;
    for (let color of colors)
    {
        console.log(color);
    }
} 

// global variable 
let myAge = 34; 

function myMumAge(){
    //console the age of my mom 
    // twice my age 

    console.log(`The age of my mum is  ${myAge*2}`)
}

myMumAge()

function twiceMyage(myAge) {
    let twice = myAge*2;
}

twiceMyage(50);
console.log("my age is :", myAge);
