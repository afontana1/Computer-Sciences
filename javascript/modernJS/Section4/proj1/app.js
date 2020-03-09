const form = document.querySelector('#task-form');
const taskList = document.querySelector('.collection');
const clearBtn = document.querySelector('.clear-tasks');
const filter = document.querySelector('#filter');
const taskInput = document.querySelector('#task');

// Load all event listeners
loadEventListeners();

function loadEventListeners(){
	//dom load event
	document.addEventListener('DOMContentLoaded',getTasks)
	form.addEventListener('submit',addTask);
	//remove task event
	taskList.addEventListener('click',removeTask);
	//Clear Task Event
	clearBtn.addEventListener('click',removeAll);
	//filter
	//on keyup because we want to filter every time something is typed in
	filter.addEventListener('keyup',Filt);

};

//get tasks from ls and show not just in
//local storage but also the UI
function getTasks(e){
	let tasks;
	if(localStorage.getItem('tasks')===null){
		tasks = [];
	}else{
		tasks = JSON.parse(localStorage.getItem('tasks'));
	}
	tasks.forEach(function(task){
		const li = document.createElement('li');
		li.className = "collection-item";
		li.appendChild(document.createTextNode(
			task
			));
		const link = document.createElement('a');
		link.className = 'delete-item secondary-content';

		link.innerHTML = '<i class="fa fa-remove"></i>';
		li.appendChild(link);

		taskList.appendChild(li)
	})
};

function addTask(e){

	if(taskInput.value === ''){
		alert('Add a Task')
	}

	const li = document.createElement('li');
	li.className = "collection-item";
	li.appendChild(document.createTextNode(
		taskInput.value
		));
	const link = document.createElement('a');
	link.className = 'delete-item secondary-content';

	link.innerHTML = '<i class="fa fa-remove"></i>';
	li.appendChild(link);

	taskList.appendChild(li)
	//local store
	storeTaskInLocalStorage(taskInput.value);
	//Clear Input
	taskInput.value = '';

	e.preventDefault();
};

function storeTaskInLocalStorage(task){
	let tasks;
	if(localStorage.getItem('tasks')===null){
		tasks = [];
	}else{
		tasks = JSON.parse(localStorage.getItem('tasks'));
	}
	tasks.push(task);
	localStorage.setItem('tasks',JSON.stringify(tasks))
};


function removeTask(e){
	if(e.target.parentElement.classList.contains("delete-item")){
		if(confirm(' are u sure')){
			var text = e.target.parentElement.parentElement.innerText;
			e.target.parentElement.parentElement.remove();
			if(localStorage.getItem('tasks')!==null){
				var memorytasks = JSON.parse(localStorage.getItem('tasks'));
				memorytasks = memorytasks.filter(function(item){
					return item !== text
				})
			localStorage.setItem('tasks',JSON.stringify(memorytasks))
			}else{
				let memorytasks = [];
				localStorage.setItem('tasks',JSON.stringify(memorytasks))
			}
		}
	}
};

function removeAll(e){
	if (confirm('u sure bubba??')){
		var tasks = document.querySelector('.collection');
		while(tasks.firstChild){
			tasks.removeChild(
				tasks.firstChild
				)
		}
	}
	localStorage.clear()
	e.preventDefault();
};

function Filter(e){
	const text = e.target.value.toLowerCase();
	document.querySelectorAll('.collection-item').forEach(
		function(task){
			const item = task.firstChild.textContent;
			if(item.toLowerCase().indexOf(text)!=-1){
				task.style.display = 'block';
			}else{
				task.style.display = 'none';

			}
		});
};

function Filt(e){
	let text = document.getElementById('filter').value.toLowerCase();
	let vals = taskList.getElementsByTagName('li');
	for(let i = 0; i<vals.length;i++){
		var candidate = vals[i].innerText.toLowerCase();
		if(candidate.includes(text)){
			vals[i].style.display = 'block'
		}else{
			vals[i].style.display = 'none'
		}
	}

};