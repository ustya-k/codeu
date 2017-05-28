import unittest
import Q1


class PermutationTest(unittest.TestCase):

	def testExampleCases(self):
		self.assertTrue(Q1.if_permutation('Listen','Silent'))
		self.assertTrue(Q1.if_permutation('Triangle',  'Integral'))
		self.assertFalse(Q1.if_permutation('Apple',  'Pabble'))


	def testCornerCases(self):
		self.assertTrue(Q1.if_permutation('', ''))
		self.assertTrue(Q1.if_permutation('abb', 'bba'))
		self.assertFalse(Q1.if_permutation('abb', 'bbba'))


	def testErrorCases(self):
		self.assertRaises(AttributeError, Q1.if_permutation, 1, 1)


if __name__ == '__main__':
	unittest.main()