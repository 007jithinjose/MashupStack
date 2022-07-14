with open('test.txt', 'r') as f:
 content = f.read().split()
freq_words = {word: content.count(word) for word in content}
print(freq_words)
f.close()