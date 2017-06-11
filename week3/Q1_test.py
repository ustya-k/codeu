import Q1
import unittest


class WordSearchTest(unittest.TestCase):		

	def testBaseCase(self):
		self.dictionary = {'CAR', 'CARD', 'CART', 'CAT', 'RAR'}
		columns = 3
		rows = 2
		lines = 'AARTCD'
		self.field = Q1.get_graph(lines, columns, rows)
		self.assertEqual({'CAR', 'CARD', 'CAT'}, Q1.get_words_in_table(self.dictionary, self.field))

	def testSingleRowCase(self):
		self.dictionary = {'AB', 'CA'}
		columns = 4
		rows = 1
		lines = 'ABCD'
		self.field = Q1.get_graph(lines, columns, rows)
		self.assertEqual({'AB'}, Q1.get_words_in_table(self.dictionary, self.field))

	def testOneCellCase(self):
		self.dictionary = {'A', 'B'}
		columns = 1
		rows = 1
		lines = 'A'
		self.field = Q1.get_graph(lines, columns, rows)
		self.assertEqual({'A'}, Q1.get_words_in_table(self.dictionary, self.field))

 
if __name__ == '__main__':
	unittest.main()