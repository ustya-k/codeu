import unittest
import Q1


class PermutationTest(unittest.TestCase):

	def testExampleCases(self):
		self.assertEqual(True, Q1.if_permutation(Q1.normalize_word('Listen'),  Q1.normalize_word('Silent')))
		self.assertEqual(True, Q1.if_permutation(Q1.normalize_word('Triangle'),  Q1.normalize_word('Integral')))
		self.assertEqual(False, Q1.if_permutation(Q1.normalize_word('Apple'),  Q1.normalize_word('Pabble')))


	def testErrorCases(self):
		self.assertRaises(TypeError, Q1.if_permutation, 1)


 
if __name__ == '__main__':
	unittest.main()