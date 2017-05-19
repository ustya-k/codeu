class Node:
	def __init__(self, value = None, next = None):
		self.value = value
		self.next = next


class LinkedList:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def clear(self):
		self.__init__()

	def add(self, x):
		self.length += 1
		if self.first == None:
			self.last = self.first = Node(x, None)
		else:
			self.last.next = self.last = Node(x, None)


def get_kth_to_last(L, k):
	L_len = L.length
	if k >= L_len or k < 0:
		return False

	el = L.first
	for i in range(L_len - k - 1):
		el = el.next
	return el.value


def main():
	L = LinkedList()
	inp = input('linkedlist elements input\n')
	while inp:
		L.add(inp)
		inp = input()
	k = int(input('k input\n'))
	
	el = get_kth_to_last(L, k)
	if el:
		print(el)
	else:
		print('there is no kth to last element')


if __name__ == '__main__':
	main()