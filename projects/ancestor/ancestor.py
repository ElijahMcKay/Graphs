# importing classes
from util import Stack, Queue


"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

	"""Represent a graph as a dictionary of vertices mapping labels to edges."""
	'''
	Example of :
		{
			1: {2},
			2: {3, 4},
			3: {5},
			4: {6, 7},
			5: {3},
			6: {3},
			7: {1, 6}
		}
	'''
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex_id):
		"""
		Add a vertex to the graph.
		"""
		if vertex_id not in self.vertices:
			self.vertices[vertex_id] = set()

	def add_edge(self, v1, v2):
		"""
		Add a directed edge to the graph.
		"""
		if v1 in self.vertices and v2 in self.vertices:
			self.vertices[v1].add(v2)
		else:
			raise Exception("ERROR: vertex does not exist")

	def add_undirected_edge(self, v1, v2):
		"""
		Add an undirected edge to the graph.
		"""
		if v1 in self.vertices and v2 in self.vertices:
			self.vertices[v1].add(v2)
			self.vertices[v2].add(v1)
		else:
			raise Exception("ERROR: vertex does not exist")

	def get_neighbors(self, vertex_id):
		"""
		Get all neighbors (edges) of a vertex.
		"""
		return self.vertices[vertex_id]

	def bft(self, starting_vertex):
		"""
		Print each vertex in breadth-first order
		beginning from starting_vertex.
		"""
		#create a queue
		q = Queue()
		# NQ the starting vertex
		q.enqueue(starting_vertex)
		# create a set to store visited vertices
		visited = set()
		# while the queue is not empty... 
		while q.size() > 0:
			# DQ the first vertex
			v = q.dequeue()
			# if it hasn't been visited NQ its neighbors
			if v not in visited:
				print(v)
				visited.add(v)
				# nq all it's neighbors
				for neighbor in self.get_neighbors(v):
					q.enqueue(neighbor)

	def dft(self, starting_vertex):
		"""
		Print each vertex in depth-first order
		beginning from starting_vertex.
		"""
		#create a stack
		q = Stack()
		# NQ the starting vertex
		q.push(starting_vertex)
		# create a set to store visited vertices
		visited = set()
		# while the stack is not empty... 
		while q.size() > 0:
			# DQ the first vertex
			v = q.pop()
			# if it hasn't been visited NQ its neighbors
			if v not in visited:
				print(v)
				visited.add(v)
				# nq all it's neighbors
				for neighbor in self.get_neighbors(v):
					q.push(neighbor)

	def dft_recursive(self, starting_vertex, visited=None):
		"""
		Print each vertex in depth-first order
		beginning from starting_vertex.
		This should be done using recursion.
		"""
		# if we just initialize the set() as default val in parameters, it will act weird with > 1 function calls and access prev values
		if visited is None:
			visited = set()

		#check if node has been visited
		if starting_vertex not in visited:
			#if not...
			# mark it as visited
			visited.add(starting_vertex)
			print(starting_vertex)
			# call dft_recursive on each neighbor
			for neighbor in self.get_neighbors(starting_vertex):
				self.dft_recursive(neighbor, visited)


	def bfs(self, starting_vertex):
		"""
		Return a list containing the shortest path from
		starting_vertex to target in
		breath-first order.
		"""
		# create a queue 
		q = Queue()
		# and add a path to the starting_vertex (order matters here)
		# neighbors = []
		# for neighbor in self.get_neighbors(starting_vertex):
		# 	neighbors.append(neighbor)
		# print('neighbors of starting node', neighbors)
		q.enqueue([starting_vertex])
		# create a set to store the visited vertices in
		visited = set()
		# while the queue is not empty
		while q.size() > 0:
			# dequeue the last vertex in the path
			path = q.dequeue()
			# if that is the the desitination vertex, return the path
			v = path[-1]
			# if that vertex has not been visited
			if v not in visited:
				# mark it as visited
				visited.add(v)

				# Add a path to all of its neighbors to the back of the queue
				for neighbor in self.get_neighbors(v):
					# make a copy of the path, so we avoid similar issues to using visited=set() in dft_recursive
					path_copy = path.copy()
					path_copy.append(neighbor)
					# enqueue the copy
					q.enqueue(path_copy)

				print(path)



	#   FIRST NOT GUARANTEED TO GIVE SHORTEST PATH
	def dfs(self, starting_vertex):
		"""
		Return a list containing a path from
		starting_vertex to destination_vertex in
		depth-first order.
		"""
		# create a queue 
		s = Stack()
		# and add a path to the starting_vertex (order matters here)
		s.push([starting_vertex])

		# while the stack is not empty
		while s.size() > 0:
			# pop the last item in stack, store in the path
			current_node = s.pop()

			if len(self.get_neighbors(current_node)) > 1:
				parents = []
				# Add a path to all of its neighbors to the back of the queue
				for neighbor in self.get_neighbors(current_node):
					parents.append(neighbor)
					# push the copy
					# s.push(path_copy)
			else:
				if len(self.get_neighbors(current_node)) == 0:
					return current_node




	def dfs_recursive(self, starting_vertex, target, visited=None, path=None):
		"""
		Return a list containing a path from
		starting_vertex to target in
		depth-first order.

		This should be done using recursion.
		"""
		if visited is None:
			visited = set()
		if path is None:
			path = []

		if starting_vertex not in visited:
			visited.add(starting_vertex)
			path_copy = path.copy()
			path_copy.append(starting_vertex)

			if starting_vertex == target:
				return path_copy

			for neighbor in self.get_neighbors(starting_vertex):
				new_path = self.dfs_recursive(neighbor, target, visited, path_copy)

				if new_path is not None:
					return new_path

			return None

'''

 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
	6   7   9

Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
'''

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
	g = Graph()

	# going to modify depth first traversal to just return every possible path

	# loop through, creating a graph
	for ancestor in ancestors:
		# build graph
		g.add_vertex(ancestor[0])
		# print('start',g.vertices)
		g.add_vertex(ancestor[1])
		g.add_edge(ancestor[1], ancestor[0])
		# print('end', g.vertices)
	
	queue = Queue()

	queue.enqueue([starting_node])

	longest_path = []

	while queue.size() > 0:
		path = queue.dequeue()
		last_node = path[-1]

		# edge case
		if len(path) > len(longest_path):
			longest_path = path
		elif len(path) == len(longest_path):
			if last_node < longest_path[-1]:
				longest_path = path

		
		for neighbor in g.get_neighbors(last_node):
			path_copy = path.copy()
			path_copy.append(neighbor)

			queue.enqueue(path_copy)
	
	if longest_path[-1] == starting_node:
		return -1
	
	return longest_path[-1]


'''

 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
	6   7   9
'''


print(earliest_ancestor(test_ancestors, 6))
"""
Return a list containing the shortest path from
starting_vertex to target in
breath-first order.
"""

# def bfs(self, starting_vertex):
# 	# create a queue 
# 	q = Queue()
# 	# and add a path to the starting_vertex (order matters here)
# 	q.enqueue([starting_vertex])
# 	# create a set to store the visited vertices in
# 	visited = set() 
# 	# while the queue is not empty
# 	while q.size() > 0:
# 		# dequeue the last vertex in the path
# 		path = q.dequeue()
# 		# if that is the the desitination vertex, return the path
# 		v = path[-1]
# 		# if that vertex has not been visited
# 		if v not in visited:
# 			# mark it as visited
# 			visited.add(v)

# 			# Add a path to all of its neighbors to the back of the queue
# 			for neighbor in self.get_neighbors(v):
# 				# make a copy of the path, so we avoid similar issues to using visited=set() in dft_recursive
# 				path_copy = path.copy()
# 				path_copy.append(neighbor)
# 				# enqueue the copy
# 				q.enqueue(path_copy)

# 			return path