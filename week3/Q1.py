def get_graph(values, n, m):
	'''
	Builds a graph.

	Args:
		values: str, elements of the table, all rows in one line
		n: int, number of columns
		m: int, number of rows

	Returns:
		dict, includes two elements with keys 'nodes' (stores a dict where key is number of a node and value is node's value) and 'vertices' (stores a dict where key is a number of a node and value is a set of numbers of nodes to which it is connected)
	'''
	nodes = {i: values[i] for i in range(n*m)}
	vertices = []
	for i in range(n*m):
		if n == 1 and m == 1:
			vertices.append({})
			break
		elif n == 1 or m == 1:
			if i == 0:
				vertices.append({i + 1})
			elif (i == m - 1 and n == 1) or (i == n - 1 and m == 1):
				vertices.append({i - 1})
			else:
				vertices.append({i - 1, i + 1})
		else:
			#up left corner
			if i == 0:
				vertices.append({i + 1, i + n, i + n + 1})
			#up right corner
			elif i == n - 1:
				vertices.append({i - 1, i + n, i + n - 1})
			#down right corner
			elif i == n*m - 1:
				vertices.append({i - 1, i - n, i - n - 1})
			#down left corner
			elif i == n*(m - 1): 
				vertices.append({i + 1, i - n, i - n + 1})
			#down sight
			elif i > n*(m - 1):
				vertices.append({i - 1, i + 1, i - n, i - n - 1, i - n + 1})
			#up sight
			elif i < n:
				vertices.append({i - 1, i + 1, i + n, i + n - 1, i + n + 1})
			#left sight
			elif i % n == 0:
				vertices.append({i + 1, i - n, i + n, i - n + 1, i + n + 1})
			#right sight
			elif (i + 1) % n == 0:
				vertices.append({i - 1, i - n, i + n, i - n - 1, i + n - 1})
			#center
			else:
				vertices.append({i - 1, i + 1, i - n, i + n, i - n - 1, i - n + 1, i + n - 1, i + n + 1})

	return {'nodes': nodes, 'vertices': vertices}


def _get_prefixes_list(dictionary):
	'''
	Gets list of all possible prefixes in dictionary.

	Args:
		dictionary: set

	Returns:
		set, all possible prefixes
	'''
	prefixes = set()
	for word in dictionary:
		for i, letter in enumerate(word):
			prefixes.add(word[:i + 1])
	return prefixes


def _isWord(line, dictionary):
	'''
	Checks if sequence of elements is a real word.

	Args:
		line: str, sequence of elements
		dictionary: set

	Returns:
		boolean
	'''
	if line in dictionary:
		return True
	else:
		return False


def _isPrefix(line, prefixes):
	'''
	Checks if sequence of elements is a possible prefix.

	Args:
		line: str, sequence of elements
		prefixes: set

	Returns:
		boolean
	'''
	if line in prefixes:
		return True
	else:
		return False


def _walk_table(line, node, table, dictionary, prefixes, visited_nodes):
	'''
	Walks through the table, looking for words.

	Args:
		line: str, sequence of elements from visited nodes
		node: int, number of the last visited node
		table: dict
		dictionary: set
		prefixes: set
		visited_nodes: set of int, nodes that had been visited and can't be used again

	Returns:
		set, words from dictionary that can be build from the chosen node
	'''
	words = set()
	if _isPrefix(line, prefixes):
		if _isWord(line, dictionary):
			words.add(line)
		for el in table['vertices'][node]:
			if el not in visited_nodes:
				new_line = line + table['nodes'][el]
				words.update(_walk_table(new_line, el, table, dictionary, prefixes, visited_nodes | {el}))
	return words



def get_words_in_table(dictionary, table):
	'''
	Gets all real words from the table.

	Args:
		dictionary: set
		table: set

	Returns:
		set, all real words in the table 
	'''
	words = set()
	prefixes = _get_prefixes_list(dictionary)
	for node in table['nodes']:
		words.update(_walk_table(table['nodes'][node], node, table, dictionary, prefixes, {node}))
	return words


def main():
	n = int(input('Input number of columns: '))
	m = int(input('Input number of rows: '))
	print('Input table row by row:')
	inp = input()
	values = ''
	while inp:
		values += inp
		inp = input()
	print('Input dictionary word by word:')
	inp = input()
	dictionary = set()
	while inp:
		dictionary.add(inp)
		inp = input()
	table = get_graph(values, n, m)
	words = get_words_in_table(dictionary, table)
	print('Words found in table:')
	for word in words:
		print(word)


if __name__ == '__main__':
	main()