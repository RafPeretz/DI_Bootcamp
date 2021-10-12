//Exercise 1 

for (let i =0 ; i<=15;i++)
{
	if(i %2 ===0)
	{
		console.log(i+ " is even ");
	}

	else 
		console.log(i+ " is odd");
}

//Exercise 2 

let shopping = ["apple", "pear", "melon", "banana"];

// 1. Loop over this array, and add to the array the word in plural ("s" at the end) of every fruit

for (let i = 0; i< shopping.length; i++)
{
	shopping[i] = shopping[i] + "s";

}
console.log(shopping);
	
