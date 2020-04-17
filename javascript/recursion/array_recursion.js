// count occurences of a number in array

var arr = [1,-2,3,4,1,2,0,5,4,5,6,-3,10,33,2];

function countOccurences(arr,target){
	if(arr.length === 0){
		return 0
	}else if(arr[0] === target){
		return 1+countOccurences(arr.slice(1,arr.length),target)
	}else{
		return countOccurences(arr.slice(1,arr.length),target)
	}
}


function reverseArray(array){
	if(array.length === 1){
		return array
	}else{
		return [array[array.length - 1]].concat(reverseArray(array.slice(0, array.length - 1)));
	}
}

console.log(reverseArray(arr))

function replaceNegs(arr){
	if(arr.length === 0){
		return [];
	}else{
		var val = arr[0];
		if(val < 0){
			return [0].concat(replaceNegs(arr.slice(1,arr.length)))
		}else{
			return [arr[0]].concat(replaceNegs(arr.slice(1,arr.length)))
		}
	}
}

console.log(replaceNegs(arr))

function average(array){
	if(array.length === 1){
		return array[0]
	}else{
		return (array[0] + average(array.slice(1))*(array.length - 1))/array.length
	}
}

console.log(average([10, 2, 3, 4, 8, 0] ))

function balanced(testVariable, startIndex = 0, currentIndex = 0) {
  // Base case1 and 2
  if (startIndex == testVariable.length) {
    return currentIndex == 0
  }

  // Base case3
  if (currentIndex < 0) { // A closing parenthesis did not find its corresponding opening parenthesis
    return false
  }

  // Recursive case1
  if (testVariable[startIndex] == "(") { 
    return balanced(testVariable, startIndex + 1, currentIndex + 1)
  }

  // Recursive case2
  else if (testVariable[startIndex] == ")") { 
    return  balanced(testVariable, startIndex + 1, currentIndex - 1)
  }

  else {
    return false // the string contained an unrecognized character
  }
}

testVariable = ["(", ")", "(", ")"]
