"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

import re
from collections import defaultdict


text = input("Text:")
print(text)
words = text.split(' ')
print(words)

d1 = dict.fromkeys(words)
print(d1)

# for word in d1.keys():
#    d1[word] = len(re.findall(word, text))

counts = defaultdict(int)
for word in re.findall('\w+', text):
    counts[word] += 1

MAX = 0
for word in d1.keys():
    print(word)
    length = len(word)
    if length > MAX:
        MAX = length
print(MAX)

sorted = sorted(counts, key=counts.get)
sorted_dict = {}
for i in sorted:
    sorted_dict[i] = counts[i]

for word in sorted_dict.keys():
    print(f'{word:{MAX}} : {sorted_dict[word]}')
