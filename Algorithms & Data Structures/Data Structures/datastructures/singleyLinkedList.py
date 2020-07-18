

class Node:
  def __init__(self, data):
    self.value = data
    self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self,element):
		new_element = Node(element)
		if not self.head:
			self.head = new_element
			return 

		most_recent = self.head
		while most_recent.next:
			most_recent = most_recent.next

		most_recent.next = new_element

	def insert_after(self,element,previous_node):
		if not previous_node:
			return
		new = Node(element)
		new.next = previous_node.next
		previous_node.next = new

	def peak_last(self):
		if not self.head:
			return
		last = self.head
		while last.next:
			last = last.next
		return last.value

	def peak_next(self,element):
		return element.next.value

	def prepend(self,element):
		new = Node(element)
		new.next = self.head
		self.head = new

	def print_list(self):
		cur_node = self.head
		while cur_node:
			print(cur_node.value)
			cur_node = cur_node.next

	def delete_by_value(self,value):
		if not self.head:
			return
		element = self.head
		if element.value == value:
			self.head = element.next
			element = None
			return 

		prior = None
		while element.next:
			prior = element
			element = element.next
			if element.value == value:
				prior.next = element.next
				break

		if element is None:
			return

	def length(self):
		if not self.head:
			return None
		count = 0
		element = self.head
		while element:
			element = element.next
			count+=1
		return count

	def swap_nodes(self, key_1, key_2):
		if key_1 == key_2:
			return 

		prev_1 = None 
		curr_1 = self.head 
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1 
			curr_1 = curr_1.next
		prev_2 = None 
		curr_2 = self.head 
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2 
			curr_2 = curr_2.next
		if not curr_1 or not curr_2:
			return 

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2

		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1
		curr_1.next, curr_2.next = curr_2.next, curr_1.next

	def reverse_list(self):
		curr_node = self.head
		previous = None
		while curr_node:
			next_node = curr_node.next
			curr_node.next = previous
			previous = curr_node
			curr_node = next_node
		self.head = previous
		return 

	def merge_sorted_lists(self,llist):
		l1 = self.head
		l2 = llist.head
		s = None
		if not l1 or not l2:
			return

		if l1 and l2:
			if l1.value <= l2.value:
				s = l1
				l1 = s.next
			else:
				s = l2
				l2 = s.next
			new_head = s
		while l1 and l2:
			if l1.value <= l2.data:
				s.next = l1
				s = l1
				l2 = s.next
			else:
				s.next = l2
				s = l2
				l2 = s.next
		if not l1:
			s.next = l2
		if not l2:
			s.next = l1
		return new_head

llist = LinkedList()
llist.insert("A")
llist.insert("B")
llist.insert("C")

llist.insert_after("D",llist.head.next)
llist.delete_by_value("D")
llist.delete_by_value("E")
llist.print_list()
llist.reverse_list()
llist.print_list()