import Q2
import unittest


class SLLTest(unittest.TestCase):

	def testBaseCases(self):
		self.assertEqual(9, Q2.get_kth_to_last(L, 0))
		self.assertEqual(0, Q2.get_kth_to_last(L, 9))

	def testKnownCases(self):
		self.assertEqual(5, Q2.get_kth_to_last(L, 4))
		self.assertEqual(3, Q2.get_kth_to_last(L, 6))
 
	def testFalseCases(self):
		self.assertEqual(False, Q2.get_kth_to_last(L, -1))
		self.assertEqual(False, Q2.get_kth_to_last(L_empty, 0))
		self.assertEqual(False, Q2.get_kth_to_last(L, 10))

 
if __name__ == '__main__':
	L = Q2.LinkedList()
	L_empty = Q2.LinkedList()

	for i in range(10):
		L.add(i)
	unittest.main()