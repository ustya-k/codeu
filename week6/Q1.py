class Move:
	'''
	Object which stores pairs of positions from and to which a car is moved.

	Fields:
		_from: int, position from which element is moved
		_to: int, position to which element is moved
	'''
	def __init__(self, from_value, to_value):
		self._from = from_value
		self._to = to_value


def _find_car_on_empty_place(init_list, final_list, empty_place, moves):
	'''
	Searches for car which is supposed to be on the place which is empty now.
	Moves it there.

	Args:
		init_list: list, current positions of the cars
		final_list: list, "correct" positions of the cars
		empty_place: int, index of empty place 
		moves: list of Moves
	'''
	car = final_list[empty_place]
	change_place = init_list.index(car)
	_move_to_empty_place(init_list, final_list, empty_place, change_place, car, moves)
	

def _move_to_empty_place(init_list, final_list, empty_place, change_place, car, moves):
	'''
	Moves car to the empty place.

	Args:
		init_list: list, current positions of the cars
		final_list: list, "correct" positions of the cars
		empty_place: int, index of empty place 
		change_place: int, position of car that needs to be moved
		car: int
		moves: list of Moves
	'''
	init_list[change_place] = 0
	init_list[empty_place] = car
	moves.append(Move(change_place, empty_place))


def _find_car_in_wrong_place(init_list, final_list, empty_place, moves):
	'''
	Searches for car which is not at it's correct place yet.
	Moves it to the empty place. 

	Args:
		init_list: list, current positions of the cars
		final_list: list, "correct" positions of the cars
		empty_place: int, index of empty place 
		moves: list of Moves

	Returns:
		boolean, True if everything's in it's place, False if it isn't 
	'''
	finished = True
	for place, car in enumerate(init_list):
		if car != final_list[place]:
			_move_to_empty_place(init_list, final_list, empty_place, place, car, moves)
			finished = False
			break
	return finished


def get_moves(init_list, final_list):
	'''
	Finds moves which will correctly rearrange cars.

	Args:
		init_list: list, current positions of the cars
		final_list: list, "correct" positions of the cars

	Returns:
		list of Moves
	'''
	moves = []
	finished = len(init_list) == 0
	while not finished:
		empty_place = init_list.index(0)
		if final_list[empty_place] != 0:
			_find_car_on_empty_place(init_list, final_list, empty_place, moves)
		else:
			finished = _find_car_in_wrong_place(init_list, final_list, empty_place, moves)
	return moves


def print_moves(moves):
	'''
	Prints moves in the correct way.

	Args:
		moves: list of Moves
	'''
	for move in moves:
		print('move from %d to %d' % (move._from, move._to))


def main():
	N = int(input('Input number of the cars: ')) + 1
	print('Input initial order of the cars:')
	init_list = []
	for i in range(N):
		car = input()
		init_list.append(int(car))
	print('Input final order of the cars:')
	final_list = []
	for i in range(N):
		car = input()
		final_list.append(int(car))
	moves = get_moves(init_list, final_list)
	print_moves(moves)


if __name__ == '__main__':
	main()