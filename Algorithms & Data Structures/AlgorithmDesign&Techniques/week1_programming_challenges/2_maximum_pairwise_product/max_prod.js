// Javascript implementation of maxprod, using node js to run code

var arr = [8,2,4,3,1,5,7,6,9,10]
function max_prod(arr){
	let prod = 0;
	for(i = 0; i<arr.length; i++) {
		for(j = i+1; j<arr.length;j++){
			if(arr[i]*arr[j] > prod ){
				prod = arr[i]*arr[j]
			}

		}
	}

	return prod
}
console.log(max_prod(arr))

function sorted(arr){
	for(i = 0; i < arr.length; i++){
		for(j = i+1; j < arr.length; j++)
			if(arr[i] > arr[j]){
				[arr[i],arr[j]] = [arr[j], arr[i]]
			}
	}

	return arr
}

function max_prod_2(arr){
	var srt_arr = sorted(arr)
	return srt_arr[srt_arr.length - 1]*srt_arr[srt_arr.length - 2]
}

function find_max(arr){
	let max = 0
	for(i = 0; i<arr.length;i++){
		if(arr[i] > max){
			max = arr[i]
		}
	}
	return max
}

function max_prod_3(arr){
	if(arr.length > 0){
		var first = find_max(arr)
		arr.pop(arr[first])
		var second = find_max(arr)
		return first*second
	}
}

console.log(max_prod_3(arr))