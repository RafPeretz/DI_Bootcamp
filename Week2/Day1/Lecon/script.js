
let addressNumber= 24;
let addressStreet = "Yavne";
let country = "Israel";

let global_adress = "I live in " + addressStreet +" "+ addressNumber +" " + country;
let global_adress2 = `I live in ${addressStreet} ${addressNumber} in  ${country}`

let pets = ["cat", "dog", "fish", "rabbit", "cow"];
pets.splice(3,1,"horse");
console.log(pets);

console.log(pets.length);
 
console.log(global_adress)
console.log(global_adress2)