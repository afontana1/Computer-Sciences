//Recursive Factorial vs iterative
var factorial = function(n) {
	if(n===0){
	    return 1;
	}else{
	    return n*factorial(n-1);
	}
}; 


function factorial(n){
	var total = 0;
	for(var i = n; i>0; i--){
		total = total*i
	}
	return total
}

//Recursive palindrome
var firstCharacter = function(str) {
    return str.slice(0, 1);
};

var lastCharacter = function(str) {
    return str.slice(-1);
};

var middleCharacters = function(str) {
    return str.slice(1, -1);
};


var isPalindrome = function(str) {
    if(str.length === 0){
        return true;
    }
    if(str.length ===  1){
        return true;
    }
    // recursive case
    if(firstCharacter(str) === lastCharacter(str)){
        return isPalindrome(middleCharacters(str));
    }else{
        return false;
    }
};

console.log(sentenceTostring("I Like Eggs"))

var sentenceTostring = function(str) {
	//used to convert the sentence into a string
	//before being used in isPalindrome
	let str_content = []
	for (var i = 0; i < str.length; i++){
		if(str[i]!= " "){
			str_content.push(str[i].toLowerCase())
		}
	}
	return str_content.join("")
};


var simplePalindrome = function(str){
	var input = sentenceTostring(str);
	var input_rev = input.split().reverse().join("");
	if(input === input_rev){
		return true;
	}else{
		return false;
	}
};
console.log(simplePalindrome("aha aha"))