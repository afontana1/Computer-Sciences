class Node {

	// constructor
	constructor(data) {
		this.data = data;
		this.next = null;
	}
}


class LinkedList {
	
	constructor() {
		this.head = null;
	}
	
	// function for appending a new node in the linked list
	appendNode(newData) {
		newNode = new Node(newData);
		if (this.head == null) {
			this.head = newNode;
			return;
		}
		
		var last = this.head;
		while (last.next != null) {
			last = last.next;
		}
		last.next =  newNode;
	}

		//function for printing the linked list
	printList() {
		temp = this.head;
		while(temp != null) {
			console.log(temp.data);
			temp = temp.next;
		}
	}
}


function helperFunction(myLinkedList, current, previous) { // This function reverses the linked list recursively
	// Base case
	if (current.next == null) { 
		myLinkedList.head = current;  
		current.next = previous; 
		return; 
    }

	next = current.next;
	current.next = previous; 
	
	// Recursive case
	helperFunction(myLinkedList, next, current); 
}

function reverse(myLinkedList) {
	// Check if the head node of the linked list is null or not
	if (myLinkedList.head == null) { 
		return; 
    }
	
	// Call the helper function --> main recursive function
	helperFunction(myLinkedList, myLinkedList.head, null); 
}

// Driver code
var list = new LinkedList();
list.appendNode(4); 
list.appendNode(3); 
list.appendNode(11); 
list.appendNode(7); 

console.log("Original Linked List:");
list.printList();

reverse(list);
console.log("\nReversed Linked List:");
list.printList();