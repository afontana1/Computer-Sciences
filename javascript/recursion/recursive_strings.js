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

