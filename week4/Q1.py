def _rename_islands(islands_map, old_name, new_name):
	'''
	Changes names of the tiles.

	Args:
		islands_map: two-dimensional list
		old_name: int
		new_name: int

	Returns:
		two-dimensional list
	'''
	for i, row in enumerate(islands_map):
		for j, tile in enumerate(row):
			if tile == old_name:
				islands_map[i][j] = new_name
	return islands_map


def _name_island(islands_map, row, column, islands, island_counter, upper_tile, left_tile):
	'''
	Gives name (which island) to the new tile, renames old tiles if needed (if islands which were seen as separate actually happen to be connected).

	Args:
		islands_map: two_dimensional list
		row: int, row of the tile
		column: int, column of the tile
		islands: set, already existing islands
		island_counter: int, last name given
		upper_tile: int, value of the tile under which is new one
		left_tile: int, value of the tile right to which is new one

	Returns:
		two-dimensional list, set, int
	'''
	if upper_tile:
		islands_map[row][column] = upper_tile

	if left_tile:
		if islands_map[row][column] == 0:
			islands_map[row][column] = left_tile
		elif islands_map[row][column] != left_tile:
			islands.discard(left_tile)
			islands_map = _rename_islands(islands_map, left_tile, islands_map[row][column])

	if islands_map[row][column] == 0:
		island_counter += 1
		islands_map[row][column] = island_counter
		islands.add(island_counter)

	return islands_map, islands, island_counter


def count_islands(tiles_map, n_rows, n_columns):
	'''
	Counts number of islands on the given map.

	Args:
		tiles_map: two-dimensional list of bools
		n_rows: int
		n_columns: int

	Returns:
		int
	'''
	islands_map = [[0 for i in range(n_columns)] for row in range(n_rows)]
	island_counter = 0
	islands = set()
	for i, row in enumerate(tiles_map):
		for j, tile in enumerate(row):
			if tile:
				upper_tile = None
				left_tile = None
				if i > 0:
					upper_tile = islands_map[i - 1][j]
				if j > 0:
					left_tile = islands_map[i][j - 1]
				islands_map, islands, island_counter = _name_island(islands_map, i, j, islands, island_counter, upper_tile, left_tile)

	return len(islands)




def main():
	n = int(input('Input number of rows: '))
	m = int(input('Input number of columns: '))
	print('Input tiles:')
	tiles_map = []
	for i in range(n):
		row = input().split()
		for i, tile in enumerate(row):
			if tile == 'True':
				row[i] = True
			elif tile == 'False':
				row[i] = False
		tiles_map.append(row)

	islands_number = count_islands(tiles_map, n, m)
	print('%d islands found' % islands_number)


if __name__ == '__main__':
	main()