//Exercise 1 : Building Management
let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}

console.log(building["numberLevels"]);

console.log(building["numberOfAptByLevel"]["1"] +" "+ building["numberOfAptByLevel"]["3"]);

console.log(building["nameOfTenants"]["1"]  )
console.log(building["numberOfRoomsAndRent"]["Dan"]["0"])

let sumofSarahAndDavid = building["numberOfRoomsAndRent"]["Sarah"]["1"] + building["numberOfRoomsAndRent"]["David"]["1"];
let sumOfDan = building["numberOfRoomsAndRent"]["Dan"]["1"]
if (sumofSarahAndDavid > sumOfDan){
  console.log(" Dan's rent");
}

//Exercise 2 : Divisible By Three

let numbers = [123, 8409, 100053, 333333333, 7]

for (let i =0; i<=numbers.length; i++)
{
 if (numbers[i] %3 ==0)
  console.log("true")

else 
  console.log("false"); 
}

//Exercise 3 : Playing With Numbers

let age = [20,5,12,43,98,55];

let sum = 0;
let max = 0 ;

for (let i =0; i<age.length; i++)
{

 sum += age[i];
 if (max <age[i])
 {

  max = age[i]

 }


}
console.log(sum);
console.log(max);