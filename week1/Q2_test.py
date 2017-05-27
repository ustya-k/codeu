import Q2
import unittest


class SLLTest(unittest.TestCase):

	def setUp(self):
		self.llist = Q2.LinkedList()
		for i in range(10):
			self.llist.add(i)
		self.empty_llist = Q2.LinkedList()

	def testBaseCases(self):
		self.assertEqual(9, Q2.get_kth_to_last(self.llist, 0))
		self.assertEqual(0, Q2.get_kth_to_last(self.llist, 9))

	def testKnownCases(self):
		self.assertEqual(5, Q2.get_kth_to_last(self.llist, 4))
		self.assertEqual(3, Q2.get_kth_to_last(self.llist, 6))
 
	def testNoneCases(self):
		self.assertEqual(None, Q2.get_kth_to_last(self.llist, -1))
		self.assertEqual(None, Q2.get_kth_to_last(self.empty_llist, 0))
		self.assertEqual(None, Q2.get_kth_to_last(self.llist, 10))

 
if __name__ == '__main__':
	unittest.main()