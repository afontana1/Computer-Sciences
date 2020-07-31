

class ArrayMethods:
	def __init__(self,arr):
		self.array = arr

	def array_advance(self):
		'''
		objective is to get to the end of the array
		in as little moves as possible
		you are constrained by the numbers in the index positions
		'''
		furthest_reached = 0
		last_idx = len(A) - 1
		i = 0
		while i <= furthest_reached and furthest_reached < last_idx:
			furthest_reached = max(furthest_reached, A[i] + i)
			i += 1
		return furthest_reached >= last_idx