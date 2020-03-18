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
		if vertex_id in self.vertices:
			return self.vertices[vertex_id]
		else: 
			print("ERROR: vertex does not exist")

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
# q = [4, 3]
# visited = {1, 2, 4 ,}


# 2



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


	def bfs(self, starting_vertex, destination_vertex):
		"""
		Return a list containing the shortest path from
		starting_vertex to target in
		breath-first order.
		"""
		# create a queue 
		q = Queue()
		# and add a path to the starting_vertex (order matters here)
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
				#check if target
				if v == destination_vertex:
					return path
				# Add a path to all of its neighbors to the back of the queue
				for neighbor in self.get_neighbors(v):
					# make a copy of the path, so we avoid similar issues to using visited=set() in dft_recursive
					path_copy = path.copy()
					path_copy.append(neighbor)
					# enqueue the copy
					q.enqueue(path_copy)



	# DEPTH FIRST NOT GUARANTEED TO GIVE SHORTEST PATH
	def dfs(self, starting_vertex, destination_vertex):
		"""
		Return a list containing a path from
		starting_vertex to destination_vertex in
		depth-first order.
		"""
		# create a queue 
		s = Stack()
		# and add a path to the starting_vertex (order matters here)
		s.push([starting_vertex])
		# create a set to store the visited vertices in
		visited = set()
		# while the queue is not empty
		while s.size() > 0:
			# pop the last vertex in the path
			path = s.pop()
			# if that is the the desitination vertex, return the path
			v = path[-1]
			# if that vertex has not been visited
			if v not in visited:
				# mark it as visited
				visited.add(v)
				#check if target
				if v == destination_vertex:
					return path
				# Add a path to all of its neighbors to the back of the queue
				for neighbor in self.get_neighbors(v):
					# make a copy of the path, so we avoid similar issues to using visited=set() in dft_recursive
					path_copy = path.copy()
					path_copy.append(neighbor)
					# push the copy
					s.push(path_copy)

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

if __name__ == '__main__':
	graph = Graph()  # Instantiate your graph
	# https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
	graph.add_vertex(1)
	graph.add_vertex(2)
	graph.add_vertex(3)
	graph.add_vertex(4)
	graph.add_vertex(5)
	graph.add_vertex(6)
	graph.add_vertex(7)
	graph.add_edge(5, 3)
	graph.add_edge(6, 3)
	graph.add_edge(7, 1)
	graph.add_edge(4, 7)
	graph.add_edge(1, 2)
	graph.add_edge(7, 6)
	graph.add_edge(2, 4)
	graph.add_edge(3, 5)
	graph.add_edge(2, 3)
	graph.add_edge(4, 6)

	'''
	Should print:
		{1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
	'''
	print(graph.vertices)

	'''
	Valid BFT paths:
		1, 2, 3, 4, 5, 6, 7
		1, 2, 3, 4, 5, 7, 6
		1, 2, 3, 4, 6, 7, 5
		1, 2, 3, 4, 6, 5, 7
		1, 2, 3, 4, 7, 6, 5
		1, 2, 3, 4, 7, 5, 6
		1, 2, 4, 3, 5, 6, 7
		1, 2, 4, 3, 5, 7, 6
		1, 2, 4, 3, 6, 7, 5
		1, 2, 4, 3, 6, 5, 7
		1, 2, 4, 3, 7, 6, 5
		1, 2, 4, 3, 7, 5, 6
	'''
	# graph.bft(1)

	'''
	Valid DFT paths:
		1, 2, 3, 5, 4, 6, 7
		1, 2, 3, 5, 4, 7, 6
		1, 2, 4, 7, 6, 3, 5
		1, 2, 4, 6, 3, 5, 7
	'''
	# graph.dft(1)
	# graph.dft_recursive(1)

	'''
	Valid BFS path:
		[1, 2, 4, 6]
	'''
	# print(graph.bfs(1, 6))

	'''
	Valid DFS paths:
		[1, 2, 4, 6]
		[1, 2, 4, 7, 6]
	'''
	print(graph.dfs(1, 6))
	# print(graph.dfs_recursive(1, 6))
	# print(graph.dfs_recursive(1, 6))
