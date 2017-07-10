class OrientedGraph:
	def __init__(self):
		self.nodes = set()

	def add(self, value, parent_value = None):
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
	def __init__(self, value = None, parents = set(), children = set()):
		self.value = value
		self.parents = parents
		self.children = children


def drop_empty_words(words):
	words = [word for word in words if word != '']
	return words


def get_ordered_letters(dictionary, letter_graph):
	same_prefix_words = []
	last_letter = None
	for word in dictionary:
		if last_letter == word[0]:
			same_prefix_words.append(word[1:])
		else:
			same_prefix_words = drop_empty_words(same_prefix_words)
			if same_prefix_words != []:
				letter_graph = get_ordered_letters(same_prefix_words, letter_graph)
			same_prefix_words = [word[1:]]
			letter_graph.add(word[0], last_letter)
			last_letter = word[0]

	same_prefix_words = drop_empty_words(same_prefix_words)
	if same_prefix_words != []:
		letter_graph = get_ordered_letters(same_prefix_words, letter_graph)
	return letter_graph


def topological_sort(graph):
	sorted_elements = []
	for node in graph.nodes:
		if node.parents == set():
			sorted_elements.append(node.value)
	graph.nodes = {node for node in graph.nodes if node.value not in sorted_elements}
	for node in graph.nodes:
		node.parents = {parent for parent in node.parents if parent.value not in sorted_elements}
	if graph.nodes:
		sorted_elements += topological_sort(graph)
	return sorted_elements


def get_alphabet(dictionary):
	letter_graph = OrientedGraph()
	letter_graph = get_ordered_letters(dictionary, letter_graph)
	alphabet = topological_sort(letter_graph)
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