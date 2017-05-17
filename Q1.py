def normalize_word(word):
	word = word.lower()
	word = sorted(word)
	return word


def main():
	word1 = normalize_word(input())
	word2 = normalize_word(input())
	if word1 == word2:
		print(True)
	else:
		print(False)


if __name__ == '__main__':
	main()
