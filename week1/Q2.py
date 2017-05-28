# element of a linked list
# consists a value of itself and a link to the next element
class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next

# data structure, consists of nodes
# clear -- resets a linked list
# add -- adds new node, adds a link to the new element to the last one (if present)
class LinkedList:
	def __init__(self):
		self.clear()

	def clear(self):
		self.first = None
		self.last = None
		self.length = 0

	def add(self, value):
		self.length += 1
		if self.first == None:
			self.first = Node(value, None)
			self.last = self.first
		else:
			self.last.next = Node(value, None)
			self.last = self.last.next


def get_kth_to_last(llist, k):
	llist_len = llist.length
	if k >= llist_len or k < 0:
		return None

	el = llist.first
	for i in range(llist_len - k - 1):
		el = el.next
	return el.value


def main():
	llist = LinkedList()
	print('input elements of your linked list:')
	inp = input()
	while inp:
		llist.add(inp)
		inp = input()
	k = int(input('input k: '))
	
	el = get_kth_to_last(llist, k)
	if el != None:
		print(el)
	else:
		print('there is no kth to last element')


if __name__ == '__main__':
	main()