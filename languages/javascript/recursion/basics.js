/*
Base Case: The base case is where further calls to the same function stop.
Recursive Case: The recursive case is where the function calls itself repeatedly 

function RecursiveFunction() {
  // Base Case
  if (<baseCaseCondition>) {
    return <some value>;
  }
 
  // Recursive Case
  else {
    return <recursive call and any other task>;
  }
*/

// Basic Example: return the nth fibonacci number

function fib(n){
	if(n<2){
		return 1
	}else if(n==2){
		return 1
	}else{
		return fib(n-1) + fib(n-2)
	}
}

console.log(fib(10))

/*
Memory allocation: stacks in computing architectures are regions of memory
where data is added or removed in a LIFO manner

Data is pushed to the top of the stack, the last object pushed to it is first one popped.
For example, suppose, we have a program as follows:

function function1(<parameters>) {
  <create some variables>
  return <some data>;
}
 
function function2(<parameters>) {
  <create some variables>
  return <some data>;
}
 
// Driver Code
function1();
function2();

----Stack----

function1() <---When function returns, its popped off stack
function2() <---When called, all of its data is pushed onto memory stack

A recursive function calls itself, therefore, the memory for a called function is allocated on top of memory allocated for calling function.
Remember, a different copy of local variables is created for each function call. 
When the base case is reached, the child function returns its value to the function from which it was called. 
Then, this child function’s stack frame is removed. This process continues until the parent function is returned.
*/

function factorial(n){
	if(n==1){
		return 1
	}else{
		return n*factorial(n-1)
	}
}
console.log(factorial(5))

/*
process:
---stack---
factorial(1)--->factorial 2 calls factorial 1
factorial(2)--->factorial 3 calls factorial 2
factorial(3)--->factorial 4 calls factorial 3
factorial(4)--->factorial 5 calls factorial 4
factorial(5)--->called first

return 1 -- > 
return 2 -- > return 1 to factorial(2) popped off top of stack
return 6 -- > return 2 to factorial(3) popped off top of stack
return 24 -- > return 6 to factorial(4) popped off top of stack
return 120 -- > return 24 to factorial(5) popped off top of stack (top of stack)

will stop recursing once base case is met
*/

/*
Direct Recursion:
This type of recursion calls itself in the function body

Indirect Recursion:
Indirect recursion (or mutual recursion) occurs when a function calls another function, eventually resulting in the original function being called again.

For example, if function function1() calls another function function2() and function2() 
eventually calls the original function function1() - this phenomenon results in indirect 
recursion (or mutual recursion).

function function1(p1, p2, ..., pn) {
  // Some code here
  function2(p1, p2, ..., pn);
  // Some code here
}
 
function function2(p1, p2, ..., pn) {
  // Some code here
  function1(p1, p2, ..., pn);
  // Some code here
}
*/
function printNaturalNumbersDirect(lowerRange, upperRange) {
  // Base case
  if(lowerRange > upperRange) {
    return;
  }
  console.log(lowerRange);

  // Recursive case
  printNaturalNumbers(lowerRange + 1, upperRange);
}

// Driver Code
var n = 5;
printNaturalNumbersDirect(1, n);

function printNaturalNumbers(lowerRange, upperRange) {
	if(lowerRange <= upperRange) {
	  console.log(lowerRange);
	  lowerRange += 1;
	  helperFunction(lowerRange, upperRange);
  }
	else {
		return;
  }
}

function helperFunction(lowerRange, upperRange) {
  if(lowerRange <= upperRange) {
    console.log(lowerRange);
    lowerRange += 1;
    printNaturalNumbers(lowerRange, upperRange);
  }
  else {
      return;
  }
}

// Driver Program 
var n = 5;
printNaturalNumbers(1, n);