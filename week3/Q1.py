def get_graph(values, n, m):
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
	prefixes = set()
	for word in dictionary:
		for i, letter in enumerate(word):
			prefixes.add(word[:i + 1])
	return prefixes


def _isWord(line, dictionary):
	if line in dictionary:
		return True
	else:
		return False


def _isPrefix(line, prefixes):
	if line in prefixes:
		return True
	else:
		return False


def _walk_table(line, node, table, dictionary, prefixes, visited_nodes):
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