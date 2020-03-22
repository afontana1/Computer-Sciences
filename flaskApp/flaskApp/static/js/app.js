console.log(
	'YOOOOOO YOUR THE ADMIN UR THE BO$$'
	);

const button = document.getElementById('button');
console.log(button)

eventListeners();

function eventListeners(){

	button.addEventListener('click',function(){
		var text = document.getElementsByTagName('p')[0];
		text.innerText = 'ur the boss'
	})
};