def normalize_word(word):
	word = word.lower()
	word = sorted(word)
	return word


def if_permutation(w1, w2):
	if w1 == w2:
		return True
	else:
		return False


def main():
	word1 = normalize_word(input())
	word2 = normalize_word(input())
	print(if_permutation(word1, word2))


if __name__ == '__main__':
	main()