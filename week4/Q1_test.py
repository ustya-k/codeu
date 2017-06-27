import Q1
import unittest


class IslandCountTest(unittest.TestCase):		

	def testBaseCase(self):
		tiles_map = [[False, True, False, True],
					[True, True, False, False],
					[False, False, True, False],
					[False, False, True, False]]
		columns = 4
		rows = 4
		
		self.assertEqual(3, Q1.count_islands(tiles_map, rows, columns))

	def testEmptyField(self):
		tiles_map = [[]]
		columns = 0
		rows = 0
		
		self.assertEqual(0, Q1.count_islands(tiles_map, rows, columns))

 
if __name__ == '__main__':
	unittest.main()