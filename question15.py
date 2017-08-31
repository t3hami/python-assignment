input_string = input('Enter a string: ')
words = input_string.split(' ')
words_frequency = []
for word in set(words):
    words_frequency.append((word, words.count(word)))
words_frequency = sorted(words_frequency, key=lambda x: x[0])
for word_frequency in words_frequency:
    print(str(word_frequency[0])+': '+str(word_frequency[1]))