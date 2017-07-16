import Q1
import unittest


class AlphabetTest(unittest.TestCase):

	def testBaseCase(self):
		dictionary = ['ART', 'RAT', 'CAR', 'CAT']
		self.assertIn(Q1.get_alphabet(dictionary), [['A', 'R', 'T', 'C'], ['A', 'R', 'C', 'T']])


	def testEmptyCase(self):
		dictionary = []
		self.assertEqual([], Q1.get_alphabet(dictionary))


if __name__ == '__main__':
	unittest.main()