//Exercise 1 : Is_Blank

function isBlank(str)
{
 if (str==='' || str.length ===0)
 {
     return 'True'
 }
    else
    {
        return 'False'
    }
}
console.log(isBlank(''));
console.log(isBlank('abc'));


//Exercise 2 : Abbrev_name

function abbrevName(name )
{
 let splitName = name.split(' ');

 if(splitName.length > 1)
 {
    return (splitName[0] + "" + splitName[1].charAt(0) + '.')
 }

 else 
 {
    return  splitName.charAt(0) + '.'
 }
}

console.log(abbrevName("Robin Singh")); 

