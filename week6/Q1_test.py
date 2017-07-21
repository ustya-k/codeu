import Q1
import unittest

def compare_objects(moves1, moves2):
	for i, move in enumerate(moves1):
		if move._from != moves2[i]._from or move._to != moves2[i]._to:
			return False
	return True


class CarRearrangeTest(unittest.TestCase):

	def testBaseCases(self):
		self.assertEqual([], Q1.get_moves([0, 1, 2, 3], [0, 1, 2, 3]))
		self.assertTrue(compare_objects([Q1.Move(1, 2), Q1.Move(0, 1), Q1.Move(3, 0)],
			Q1.get_moves([1, 2, 0, 3], [3, 1, 2, 0])))
 
	def testNoneCases(self):
		self.assertEqual([], Q1.get_moves([0], [0]))

 
if __name__ == '__main__':
	unittest.main()