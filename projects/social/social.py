import random
from util import Queue

class User:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"{self.name}"

class SocialGraph:
	def __init__(self):
		self.last_id = 0
		self.users = {}
		self.friendships = {}

	def add_friendship(self, user_id, friend_id):
		"""
		Creates a bi-directional friendship
		"""
		if user_id == friend_id:
			print("WARNING: You cannot be friends with yourself")
		elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
			print("WARNING: Friendship already exists")
		else:
			self.friendships[user_id].add(friend_id)
			self.friendships[friend_id].add(user_id)

	def add_user(self, name):
		"""
		Create a new user with a sequential integer ID
		"""
		self.last_id += 1  # automatically increment the ID to assign the new user
		self.users[self.last_id] = User(name)
		self.friendships[self.last_id] = set()

	def populate_graph(self, num_users, avg_friendships):
		"""
		Takes a number of users and an average number of friendships
		as arguments

		Creates that number of users and a randomly distributed friendships
		between those users.

		The number of users must be greater than the average number of friendships.
		"""
		# Reset graph
		self.last_id = 0
		self.users = {}
		self.friendships = {}
		# !!!! IMPLEMENT ME

		# Add users
		for user in range(num_users):
			# print(user)
			self.add_user(user + 1)

		# print(self.users)
		# var to store all possible friendships
		possible_friendships = []
		# Create friendships
		for user_id in self.users:
			for friend_id in range(user_id + 1, self.last_id + 1):
				if user_id < friend_id:
					possible_friendships.append((user_id, friend_id))

		random.shuffle(possible_friendships)

		for i in range(num_users * avg_friendships // 2):
			friendship = possible_friendships[i]
			self.add_friendship(friendship[0], friendship[1])

		# print('possible friendships', possible_friendships)



	def get_all_social_paths(self, user_id):
		"""
		Takes a user's user_id as an argument

		Returns a dictionary containing every user in that user's
		extended network with the shortest friendship path between them.

		The key is the friend's ID and the value is the path.
		"""
		# find every path where len(path) > 1
		visited = {}  # Note that this is a dictionary, not a set
		# !!!! IMPLEMENT ME
		# creating a queue
		queue = Queue()
		# start off by adding current path (just user_id) to the queue
		queue.enqueue([user_id])

		while queue.size() > 0:
			# capturing current path a variable
			friend_path = queue.dequeue()

			# if not in visited
			if friend_path[-1] not in visited:

				visited[friend_path[-1]] = friend_path

				# friend_path_copy = []
				for friend in self.friendships[user_id]:
					friend_path_copy = friend_path.copy()
					friend_path_copy.append(friend)
					queue.enqueue(friend_path_copy)
					print('friend', friend_path_copy)

			# print('self users', self.users)
		return visited


if __name__ == '__main__':
	sg = SocialGraph()
	sg.populate_graph(10, 2)
	# print(sg.friendships)
	connections = sg.get_all_social_paths(4)
	print(sg.friendships)
	print(connections)
