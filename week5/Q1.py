class OrientedGraph:
	'''
	Implementation of oriented graph. All of the nodes have unique values.

	Fields:
		nodes: set of Nodes, all nodes of the graph
	'''
	def __init__(self):
		self.nodes = set()

	def add(self, value, parent_value = None):
		'''
		Adds new Node to the OrientedGraph or updates existing ones.

		Args:
			value: str
			parent_value: str
		'''
		node = None
		parent = None
		for inode in self.nodes:
			if inode.value == value:
				node = inode
			if inode.value == parent_value:
				parent = inode

		if parent_value:
			if node:
				node.parents = node.parents.union({parent})
				parent.children = parent.children.union({node})
			else:
				node = Node(value, parents = {parent})
				parent.children = parent.children.union({node})
				self.nodes.add(node)
		else:
			if not node:
				node = Node(value)
				self.nodes.add(node)


class Node:
	'''
	Element of OrientedGraph.

	Fields:
		value: str
		parents: set of Nodes, from which Node has incoming edges
		children: set of Nodes, to which Node has outcoming edges
	'''
	def __init__(self, value = None, parents = set(), children = set()):
		self.value = value
		self.parents = parents
		self.children = children


def _drop_empty_words(words):
	'''
	Removes empty elements from list.

	Args:
		words: list

	Returns:
		list
	'''
	words = [word for word in words if word != '']
	return words


def _get_ordered_letters(dictionary, letter_graph):
	'''
	Builds oriented graph with no cycles which represents hierarchy of letters.

	Args:
		dictionary: list, words in lexicogrpahic order
		letter_graph: OrientedGraph

	Returns:
		OrientedGraph
	'''
	same_prefix_words = []
	last_letter = None
	for word in dictionary:
		if last_letter == word[0]:
			same_prefix_words.append(word[1:])
		else:
			same_prefix_words = _drop_empty_words(same_prefix_words)
			if same_prefix_words != []:
				letter_graph = _get_ordered_letters(same_prefix_words, letter_graph)
			same_prefix_words = [word[1:]]
			letter_graph.add(word[0], last_letter)
			last_letter = word[0]

	same_prefix_words = _drop_empty_words(same_prefix_words)
	if same_prefix_words != []:
		letter_graph = _get_ordered_letters(same_prefix_words, letter_graph)
	return letter_graph


def _topological_sort(graph):
	'''
	Builds a possible alphabet from given letter hierarchy.

	Args:
		graph: OrientedGraph

	Returns:
		list
	'''
	sorted_elements = []
	for node in graph.nodes:
		if node.parents == set():
			sorted_elements.append(node.value)
	graph.nodes = {node for node in graph.nodes if node.value not in sorted_elements}
	for node in graph.nodes:
		node.parents = {parent for parent in node.parents if parent.value not in sorted_elements}
	if graph.nodes:
		sorted_elements += _topological_sort(graph)
	return sorted_elements


def get_alphabet(dictionary):
	'''
	Builds a possible alphabet from given dictionary.

	Args:
		dictionary: list, words in lexicogrpahic order

	Returns:
		list
	'''
	letter_graph = OrientedGraph()
	letter_graph = _get_ordered_letters(dictionary, letter_graph)
	alphabet = _topological_sort(letter_graph)
	return alphabet


def main():
	dictionary = []
	print('Input dictionary word by word:')
	word = input()
	while word:
		dictionary.append(word)
		word = input()
	print(' '.join(get_alphabet(dictionary)))


if __name__ == '__main__':
	main()