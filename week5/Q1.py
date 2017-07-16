from OrientedGraph import OrientedGraph

def _add_ordered_letters(dictionary, letter_graph):
	'''
	Builds oriented graph with no cycles which represents hierarchy of letters.

	Args:
		dictionary: list, words in lexicogrpahic order
		letter_graph: OrientedGraph, to which new edges are added based on the words
      in the dictionary

	Returns:
		OrientedGraph
	'''
	same_prefix_words = []
	last_letter = None
	for word in dictionary:
		if last_letter != word[0] :
			_add_ordered_letters(same_prefix_words, letter_graph)
			same_prefix_words = []
			letter_graph.add(word[0], last_letter)
			last_letter = word[0]
		if len(word[1:]) > 0:
			same_prefix_words.append(word[1:])

	if dictionary:
		_add_ordered_letters(same_prefix_words, letter_graph)


def _check_if_has_no_parents(node, sorted_elements):
	'''
	Checks if node has any parents which had't been sorted yet. 

	Args:
		node: Node
		sorted_elements: list, elements that had already been sorted

	Returns:
		boolean, True if it doesn't have parents, False if it does
	'''
	for parent in node.parents:
		if parent.value not in sorted_elements:
			return False
	return True


def _topological_sort(graph):
	'''
	Builds a possible alphabet from given letter hierarchy.

	Args:
		graph: OrientedGraph

	Returns:
		list, the ordered letters of the unknown alphabet
	'''
	sorted_elements = []
	while len(graph.nodes) > len(sorted_elements):
		# Search for letters which do not have any preceding letters at this step.
		new_sorted_elements = []
		for node in graph.nodes:
			if node.value not in sorted_elements and _check_if_has_no_parents(node, sorted_elements):
				new_sorted_elements.append(node.value)
		sorted_elements += new_sorted_elements
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
	_add_ordered_letters(dictionary, letter_graph)
	return _topological_sort(letter_graph)


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