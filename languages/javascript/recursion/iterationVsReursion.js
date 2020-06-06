/*
The concept of Recursion and Iteration is to execute a set of instructions repeatedly.

However, the difference between them is that recursion is simply a method call in which the method being called is the same as the one making the call. 
Iteration, on the other hand, is when a loop is repeatedly executed until a certain condition is satisfied.

Both recursion and iteration depend on a condition which determines whether to stop execution or continue it.

function IterativeFunction() {
   //some local variables if required
  while (<someCondition == true>) {
    // Perform a task
  }
}
*/

function factorial(targetNumber) {
  var index = targetNumber - 1; // set the index to target - 1
  
  while(index >= 1) {
    targetNumber = targetNumber * index; // multiply targetNumber with one less than itself,
                                            // i.e, index here
    index -= 1; // reduce index in each iteration
  }
  
  return targetNumber;
}

// Driver Code
var targetNumber = 5;
var result = factorial(targetNumber);
console.log("The factorial of " + targetNumber + " is: " + result);

//Reverse String

function iterativeReverse(str){
	var result = "" ;
	var strLen = str.length;
	while(strLen>=0){
		result+=str.charAt(strLen)
		strLen-=1
	}

	return result
}

console.log(iterativeReverse("AJ"))

function recursiveReverse(str){
	if(str.length===0){
		return str
	}else{
		return str.charAt(str.length-1)+recursiveReverse(str.slice(0,str.length-1))
	}
}

console.log(recursiveReverse("AJ"))

// Count the number of vowels in a string
// return an object containing the vowel and the count

function countVowelsIteration(str){
	var str = str.toLowerCase();
	var vowels = "aeiou";
	var output = {};
	for(i=0;i<str.length;i++){
		char = str[i]
		if(vowels.indexOf(char)!=-1){
			if(char in output){
				output[char]+=1
			}else{
				output[char] = 1
			}
		}
	}
	return output
}

console.log(countVowelsIteration("AJAJBJIJ"))

function countVowelsRecursion(str, output = {}){
	var str = str.toLowerCase();
	var vowels = "aeiou";
	var firstLetter = str[0]
	if(str.length===1){
		return output
	}else if(vowels.indexOf(firstLetter)!=-1){
		if(firstLetter in output){
			output[firstLetter]+=1
			return countVowelsRecursion(str.slice(1,str.length),output)
		}else{
			output[firstLetter] = 1
			return countVowelsRecursion(str.slice(1,str.length),output)
		}
	}else{
		return countVowelsRecursion(str.slice(1,str.length),output)
	}
	return output;
}

console.log(countVowelsRecursion("AJAJBJIJ"))

/*
function isVowel(character) { // function to check whether input character is a vowel
  var character = character.toLowerCase(); // convert character to lower case so upper cases can also be handled
  var vowels = "aeiou"; // string containing all vowels

  if (vowels.indexOf(character) != -1) { // check if given character is in vowels
    return true;
  }
  else {
      return false;
  }
}

//iterative solution
function countVowels(string) { // function that returns the count of vowels
	var count = 0;
	for (var i = 0; i < string.length; i++) {
		if (isVowel(string[i])) { // check if character is vowel 
			count += 1;
    }
  }
  return count; 
}

// Driver code 
var targetVariable = "Educative";
console.log(countVowels(targetVariable));

// recursive solution
function countVowels(string, stringLength) { //function that returns the count of vowels
	// Base case
  if (stringLength == 1) {
	  return Number(isVowel(string[0])); 
  }

  // Recursive case
  return countVowels(string, stringLength - 1) + isVowel(string[stringLength - 1]); 
}

// Driver code 
var string = "Educative";
console.log(countVowels(string, string.length)); 
*/

//Computing the square of a number
var count = 0;
function computeSquare(num){
	count+=1
	if(count === num){
		return num
	}else{
		return num + computeSquare(num)
	}
}

console.log(computeSquare(5))

function raiseToPower(num,target){
	if(target === 1){
		return num;
	}else{
		return num*raiseToPower(num,target-1)
	}
}

console.log(raiseToPower(5,4))

// First occurence of an element in an array
function main(inputArray,element){
	var index = 0;
	function searchForElement(inputArray,element){
		if(index > inputArray.length){
			return -1
		}else if(inputArray[index] === element){
			return index
		}else{
			index+=1;
			return searchForElement(inputArray,element)
		}

	}
	return searchForElement(inputArray,element);
}
var arr = [1,2,3,45,6,6,6,8,7];
console.log(main(arr,9))

/*
function firstIndex(arr, testVariable, currentIndex) { // returns the first occurrence of testVariable
  
  while (currentIndex < arr.length) { // Iterate over the array
    if (arr[currentIndex] == testVariable) {  // Return the current index if testVariable found
      return currentIndex;
    } 
    currentIndex += 1;
  }
}

// Driver Code
var arr = [9, 8, 1, 8, 1, 7];
var testVariable = 1;
var currentIndex = 0;
console.log(firstIndex(arr, testVariable, currentIndex));
*/

function fibonacciIterative(n){
	var first = 0;
	var second = 1;
	var i = 0;
	while(i<n-1){
		var nth = second + first;
		first = second
		second = nth
		i+=1
	}
	return nth
}

console.log(fibonacciIterative(7))