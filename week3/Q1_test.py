import Q1
import unittest


class WordSearchTest(unittest.TestCase):		

	def testBaseCase(self):
		dictionary = {'CAR', 'CARD', 'CART', 'CAT', 'RAR'}
		columns = 3
		rows = 2
		lines = 'AARTCD'
		field = Q1.get_graph(lines, columns, rows)
		self.assertEqual({'CAR', 'CARD', 'CAT'}, Q1.get_words_in_table(dictionary, field))

	def testSingleRowCase(self):
		dictionary = {'AB', 'CA'}
		columns = 4
		rows = 1
		lines = 'ABCD'
		field = Q1.get_graph(lines, columns, rows)
		self.assertEqual({'AB'}, Q1.get_words_in_table(dictionary, field))

	def testOneCellCase(self):
		dictionary = {'A', 'B'}
		columns = 1
		rows = 1
		lines = 'A'
		field = Q1.get_graph(lines, columns, rows)
		self.assertEqual({'A'}, Q1.get_words_in_table(dictionary, field))

	def testEmptyField(self):
		dictionary = {'A', 'B'}
		columns = 0
		rows = 0
		lines = ''
		field = Q1.get_graph(lines, columns, rows)
		self.assertEqual(set(), Q1.get_words_in_table(dictionary, field))

 
if __name__ == '__main__':
	unittest.main()