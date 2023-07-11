"""
Word Occurrences
Estimate: 30 minutes
Actual:   1hr minutes
"""

import re
from collections import defaultdict

text = input("Text:")
words = text.split(' ')

d1 = dict.fromkeys(words)

counts = defaultdict(int)
for word in re.findall('\w+', text):
    counts[word] += 1

# find the length of the longest word
MAX = 0
for word in d1.keys():
    length = len(word)
    if length > MAX:
        MAX = length

# sorted the output
sorted_list = sorted(counts, key=counts.get)
sorted_dict = {}
for i in sorted_list:
    sorted_dict[i] = counts[i]

# use f-string to print the result
for word in sorted_dict.keys():
    print(f'{word:{MAX}} : {sorted_dict[word]}')
