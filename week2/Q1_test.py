import Q1
import unittest


class BTTest(unittest.TestCase):

	def setUp(self):
		self.binary_tree = Q1.BinaryTree(16)
		self.binary_tree.left = Q1.BinaryTree(9)
		self.binary_tree.left.left = Q1.BinaryTree(3)
		self.binary_tree.left.left.left = Q1.BinaryTree(1)
		self.binary_tree.left.left.right = Q1.BinaryTree(5)
		self.binary_tree.left.right = Q1.BinaryTree(14)
		self.binary_tree.right = Q1.BinaryTree(18)
		self.binary_tree.right.right = Q1.BinaryTree(19)

	def testBaseCases(self):
		self.assertEqual([], Q1.get_ancestors(self.binary_tree, 16))
		self.assertEqual([3, 9, 16], Q1.get_ancestors(self.binary_tree, 5))
		self.assertEqual([16], Q1.get_ancestors(self.binary_tree, 18))
 
	def testNoneCases(self):
		self.assertEqual(None, Q1.get_ancestors(self.binary_tree, 13))

 
if __name__ == '__main__':
	unittest.main()