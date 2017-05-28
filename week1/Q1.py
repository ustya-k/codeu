def normalize_word(word):
	word = word.lower()
	word = sorted(word)
	return word


# gets two strings
# checks if one is a permutation of the other
# returns boolean value
def if_permutation(w1, w2):
	w1 = normalize_word(w1)
	w2 = normalize_word(w2)
	return w1 == w2


def main():
	word1 = input('write 1st word\n')
	word2 = input('write 2nd word\n')
	print(if_permutation(word1, word2))


if __name__ == '__main__':
	main()