
//exercise 1 
let sentence = prompt('Please give me a sentence with the word nemo');
let hastest = sentence.includes("nemo");

if(hastest==true)

{
  let indexOfFirst = sentence.split(' ').indexOf('nemo');
    console.log(`I found nemo at the ${indexOfFirst+1} place !`) ;
}
else 
{
    console.log("nemo not find" )
}

  
  //Exercise 1 : Evaluation


  console.log(5 >= 1);
  console.log(0 === 1);
  console.log(4 <= 1);
  console.log(1 != 1);
  console.log("A" > "B");
  console.log("B" < "C");
  console.log("a" > "A");
  console.log("b" < "A");
  console.log(true === false);
  console.log(true != true);



//Exercise 2 : Evaluation(2)
let c;
    let a = 34;
    let b = 21;
    a = 2;
   let d = a + b
    console.log (d);
    console.log(c);
    console.log(3 + 4 + '5');



//Exercise 3 : Ask For Numbers

let number = prompt("Give me a string of number separated by commas");
number = number.split(",");
let res = 0;
for (let i=0; i<number.length;i++){
    if(+number[i]){
    res+= +number[i];
};
};

console.log((res));

//Exercise 4 : Boom

num = parseInt(prompt('Choose a number'));
if (num<2) {
    console.log('boom')}
else {

    if ((num%5 ===0 && num%2===0)){
        console.log(('b'+'o'.repeat(num)+'m!').toUpperCase())
    }

    else if (num%2 === 0){
        console.log('b'+'o'.repeat(num)+'m!')
    }
    
    else if (num%5 === 0){
        console.log(('b'+'o'.repeat(num)+'m').toUpperCase())
    }

    else{
        console.log('b'+'o'.repeat(num)+'m')

    }
}