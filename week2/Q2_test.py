import Q2
import unittest


class BTTest(unittest.TestCase):

	def setUp(self):
		self.binary_tree = Q2.BinaryTree(16)
		self.binary_tree.left = Q2.BinaryTree(9)
		self.binary_tree.left.left = Q2.BinaryTree(3)
		self.binary_tree.left.left.left = Q2.BinaryTree(1)
		self.binary_tree.left.left.right = Q2.BinaryTree(5)
		self.binary_tree.left.right = Q2.BinaryTree(14)
		self.binary_tree.right = Q2.BinaryTree(18)
		self.binary_tree.right.right = Q2.BinaryTree(19)

	def testBaseCases(self):
		self.assertEqual(9, Q2.get_common_ancestor(self.binary_tree, 5, 14))
		self.assertEqual(Q2.get_common_ancestor(self.binary_tree, 5, 14), Q2.get_common_ancestor(self.binary_tree, 14, 5))
		self.assertEqual(16, Q2.get_common_ancestor(self.binary_tree, 9, 16))
 
	def testNoneCases(self):
		self.assertEqual(None, Q2.get_common_ancestor(self.binary_tree, 1, 13))

 
if __name__ == '__main__':
	unittest.main()