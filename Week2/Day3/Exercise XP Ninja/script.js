// Exercise 1 : Checking The BMI
let man = 
{
    FullName :"Samuel",
    Mass:70,
    Height:1.80,
    BMI : function ()
    {
       return (this.Mass*this.Height*this.Height*10000);
    }
}

let girl =
 {
    FullName :"Ilona",
    Mass:75,
    Height:1.80,
    BMI : function ()
    {
       return (this.Mass*this.Height*this.Height*10000);
    }
 }

if(girl.BMI()>man.BMI())

{
    console.log(girl["FullName"]+" has a biger bmi")
}
else
{
    console.log(man["FullName"]+" has a biger bmi")
}


//Exercise 2 : Grade Average

function findAvg (gradelist)
{

 let sum = 0;
 let count = 0; 
 let average = 0;

 for (let i =0; i<gradelist.length; i++)
 {
     sum += gradelist[i];
     count ++;
 }

 average = sum / count;

 return average;
}

let grade = [80 ,85];   
let avg = findAvg(grade);
console.log(avg);

if (avg > 65)
console.log("You can pass");

else 
console.log("You must repeat the course");
