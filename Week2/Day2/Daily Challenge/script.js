let sentence = "This movie is not so bad !";
let bad = "bad";
let not = "not";
let str1 ="";
let str2 ="";
let start = sentence.search(not);
let end = sentence.search(bad);
if( start < end ){
	str1 = sentence.slice(0 , start);
	str2 = sentence.slice(end+3, sentence.length);
	console.log(str1+"good"+str2)

}else{
	console.log(sentence)
}