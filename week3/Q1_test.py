import Q1
import unittest


class WordSearchTest(unittest.TestCase):

	def setUp(self):
		self.dictionary = {'CAR', 'CARD', 'CART', 'CAT'}
		columns = 3
		rows = 2
		lines = 'AARTCD'
		self.field = Q1.get_graph(lines, columns, rows)
		

	def testBaseCases(self):
		self.assertEqual({'CAR', 'CARD', 'CAT'}, Q1.get_words_in_table(self.dictionary, self.field))
		#self.assertEqual(Q2.get_common_ancestor(self.binary_tree, 5, 14), Q2.get_common_ancestor(self.binary_tree, 14, 5))
		#self.assertEqual(16, Q2.get_common_ancestor(self.binary_tree, 9, 16))

 
if __name__ == '__main__':
	unittest.main()