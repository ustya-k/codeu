import Q1
import unittest


class AlphabetTest(unittest.TestCase):

	def testBaseCase(self):
		dictionary = ['ART', 'RAT', 'CAR', 'CAT']
		self.assertEqual(['A', 'R', 'T', 'C'], Q1.get_alphabet(dictionary))


	def testEmptyCase(self):
		dictionary = []
		self.assertEqual([], Q1.get_alphabet(dictionary))


if __name__ == '__main__':
	unittest.main()