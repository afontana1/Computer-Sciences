/*

Remove whitespaces

*/

function removeWhites(string){
	if(string.length === 1){
		return string
	}else{
		var check = string[0];
		if(check === " " || check === "\t"){
			var string = string.slice(1,string.length)
			return removeWhites(string)
		}else{
			return check + removeWhites(string.slice(1,string.length))
		}
	}
}


/*
remove adjacent duplicates
*/

var st = "Heeellloooo"

function removeDuplicates(string) {
  // Base case
  if (string.length <= 1) {
      return string;
  }

  // Recursive case1
  else if (string[0] == string[1]) {
      return removeDuplicates(string.substr(1));
  }

  // Recursive case2
  return string[0] + removeDuplicates(string.substr(1));
}


/*
Merge two sorted strings lexicographically
*/

var s1 = "abyWz"
var s2 = "AbbCH"


function merge(string1, string2) {
  // Base case1
  if (string1.length == 0) {
    if (string2.length == 0) { 
      return "";
    }
    return string2;
  }

  // Base case2
  else if (string2.length == 0) {
    return string1;
  }

  // Recursive case1
  else if (string1[0] > string2[0]) {
    return string2[0] + merge(string1, string2.substr(1));
  }

  // Recursive case2
  else {
    return string1[0] + merge(string1.substr(1), string2);
  }
}

console.log(merge(s1,s2))

/*
Length of a string
*/

function lenOfString(string){
	if(string.length === 0){
		return 0;
	}else{
		return 1 + lenOfString(string.substr(1,string.length))
	}
}

console.log(lenOfString(s1))

function IsPalindrome(string){
	if(string.length === 1){
		return true;
	}else if(string[0] != string[string.length-1]){
		return false;
	}else{
		return IsPalindrome(string.substr(1,string.length-2))
	}
}

console.log(IsPalindrome("madam"))

function replaceString(string,a,b){
	if(string.length === 0){
		return "";
	}else if(string[0] === a){
		return b + replaceString(string.substr(1),a,b)
	}else{
		return string[0] + replaceString(string.substr(1),a,b)
	}
}
console.log(replaceString("madam","a","b"))
