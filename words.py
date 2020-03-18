from util import Stack, Queue  

# undirected
# cyclic
# sparse

# using bfs because it is guaranteed to give shortest path, dfs is not

# 2: Build the Grpah
# load words from dictionary
f = open('words.txt', 'r')
words = f.read().lower().split('\n')
f.close()

#3: Traverse the graph (BFS)

def get_neighbors(word):
    """
    Get all words that are 1 letter away
    """
    # get same length words first
    same_length_words = []

    # build an adjacency list with words 1 letter away


def words_are_neighbors(w1, w2):
    '''
    return True if words are 1 letter apart
    False otherwise
    '''
    list_word = list(w1)
    # go through each letter,
    for i in range(len(list_word)):
    # swap with each letter in alphabet
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            # check if that equals given word
            temp_word = list_word.copy()
            temp_word[i] = letter

            if ''.join(temp_word) == w2:
                return True

    return False


def bfs(start_word, end_word):
    """
    Return a list containing the shortest path from
    starting_vertex to target in
    breath-first order.
    """
    # create a queue 
    q = Queue()
    # NQ start of path
    q.enqueue(start_word)

    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        # check if last word in path is the end word
        if path[-1] == end_word:
            return path[-1]

        if path[-1] not in visited:
            # NQ each neighboring word
            for neighbor in get_neighbors(path[-1]):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)





