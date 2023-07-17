"""
Word occurrences
Estimate: 30minutes
Actual:   1hr minutes
"""

word_count = {}
text = str(input("Text: "))

text = text.split()

for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_length_word = max(text, key=len)

for word, count in sorted(word_count.items()):
    print(f"{word:{len(max_length_word) + 1}}: {count}")
