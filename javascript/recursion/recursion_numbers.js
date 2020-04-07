/*
Power of a number
*/

function power(n,exponent){
	if(exponent === 0){
		return 1;
	}else{
		return n*power(n,exponent-1);
	}
}

function powerIterative(n,exponent){
	var base = n;
	var i = 1;
	while( i < exponent){
		base*=n
		i+=1
	}
	return base
}

function powerDynamic(n,exponent){
	var store = [];
	store[0] = n
	for(var i = 1; i < exponent; i++){
		store[i] = store[i-1]*n
	}
	return store.slice(-1)[0]
}

/*
sum integers 1 to n
*/

function sum_n(n){
	if(n===1){
		return 1;
	}else{
		return n + sum_n(n-1)
	}
}


function sum_n_iter(n){
	var tot = 0;
	var i = 0;
	while(i < n){
		tot+=n-i
		i+=1
	}
	return tot
}


/*
modulo operator
*/

function modulo(dividend,divisor){
	if(dividend - divisor === 0){
		return 0;
	}else if(dividend - divisor < 0){
		return dividend;
	}else{
		return modulo(dividend - divisor,divisor)
	}
}

function modulo_iterative(dividend,divisor){
	if(divisor > dividend){
		return divisor;
	}
	while(true){
		var result = dividend - divisor;
		if(result < 0){
			return dividend;
		}else if( result === 0){
			return 0;
		}
		dividend = result
	}
}

/*
Greatest common divisor:
largest common number that divides both integers
*/

function GCD_iterative(num1,num2){
	var smol = Math.min(num1,num2);
	var lorge = Math.max(num1,num2);

	var check = smol;
	var i = 1;
	while(smol > 0){
		var mod1 = modulo(smol,check)
		var mod2 = modulo(lorge,check)
		if(mod1 === 0 && mod2 === 0){
			return check;
		}
		check-=i
		i+=1
	}
	return 
}

function GCD(num1,num2){
	// when the numbers re the same their modular is same
	if(num1 === num2){
		return num1
	}else if(num1 > num2){
		return GCD(num1 - num2,num2)
	}else if(num1 < num2){
		return GCD(num1,num2 - num1)
	}
}

//console.log(GCD(42,56))

/*
Implement a function that takes a number testVariable and returns that row of the Pascal’s triangle
*/

function pascal_iterative(testVariable){
	var i = 0;
	var store = [];
	while(i <= testVariable){
		if(i === 0){
			store.push([1])
		}else if( i === 1){
			store.push([1,1])
		}else{
			var temp = [];
			temp.push(1)
			for(var j = 1; j < store[i-1].length ; j++){
				temp.push(store[i-1][j-1] + store[i-1][j])
			}
			temp.push(1)
			store.push(temp)
		}
		i+=1
		console.log(store)
	}

	return store[testVariable]
}


function Pascal(testVariable) {
  if (testVariable == 0) {
      return [1];
  }

  else {
    var line = [1];
    previousLine = Pascal(testVariable - 1);

    for (let i = 0; i < previousLine.length - 1; i++) {
      line.push(previousLine[i] + previousLine[i + 1]);
    }

    line.push(1);
  } 
  return line;
}

function convertToBinary(number){
	if(number <= 1){
		return "1"
	}else{
		var mod = modulo(number,2)
		if(mod === 0){
			var b = "0";
		}else{
			var b = "1";
		}

		return convertToBinary(Math.floor(number/2)) + b
	}
}

console.log(convertToBinary(156))