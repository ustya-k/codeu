def get_graph(grid, n, m):
	'''
	Builds a graph.

	Args:
		grid: str, elements of the grid,
				all elements in one line: 
				elements of the first row from left to right, then elements of the second row, etc.
		n: int, number of columns
		m: int, number of rows

	Returns:
		dict, includes two elements with keys 
		'nodes' (stores a dict where key is number of a node and value is node's value) 
		and 'vertices' (stores a dict where key is a number of a node 
						and value is a set of numbers of nodes to which it is connected)

	'''
	nodes = {i: grid[i] for i in range(n*m)}
	vertices = []
	for i in range(n*m):
		# if there is only one cell
		if n == 1 and m == 1:
			vertices.append({})
			break
		# if there is only one line or one row
		elif n == 1 or m == 1:
			# first cell
			if i == 0:
				vertices.append({i + 1})
			# last cell
			elif (i == m - 1 and n == 1) or (i == n - 1 and m == 1):
				vertices.append({i - 1})
			# middle cells
			else:
				vertices.append({i - 1, i + 1})
		else:
			neighbours = set()
			row = i // n
			column = i - n * row
			# above left cell
			if row - 1 >= 0 and (i - n - 1) // n == row - 1:
				neighbours.add(i - n - 1)
			# above cell
			if row - 1 >= 0:
				neighbours.add(i - n) 
			# above right cell
			if row - 1 >= 0 and (i - n + 1) // n == row - 1:
				neighbours.add(i - n + 1) 
			# left cell
			if (i - 1) // n == row:
				neighbours.add(i - 1)
			# right cell
			if (i + 1) // n == row:
				neighbours.add(i + 1)
			# below left cell
			if row + 1 < m and (i + n - 1) // n == row + 1:
				neighbours.add(i + n - 1)
			# below cell
			if row + 1 < m:
				neighbours.add(i + n) 
			# below right cell
			if row + 1 < m and (i + n + 1) // n == row + 1:
				neighbours.add(i + n + 1) 

			vertices.append(neighbours)

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
		for i in range(len(word)):
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
	return line in dictionary


def _isPrefix(line, prefixes):
	'''
	Checks if sequence of elements is a possible prefix.

	Args:
		line: str, sequence of elements
		prefixes: set

	Returns:
		boolean
	'''
	return line in prefixes


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
		for letter in table['vertices'][node]:
			if letter not in visited_nodes:
				new_line = line + table['nodes'][letter]
				words.update(_walk_table(new_line, letter, table, dictionary, prefixes, visited_nodes | {letter}))
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
	grid = ''
	while inp:
		grid += inp
		inp = input()
	print('Input dictionary word by word:')
	inp = input()
	dictionary = set()
	while inp:
		dictionary.add(inp)
		inp = input()
	table = get_graph(grid, n, m)
	words = get_words_in_table(dictionary, table)
	print('Words found in table:')
	for word in words:
		print(word)


if __name__ == '__main__':
	main()