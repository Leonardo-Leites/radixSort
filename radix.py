import string
import re
from collections import Counter

fileName = ["frankestein_clean.txt", "war_and_peace_clean.txt"]
output = ["frankestein_ordenado.txt","war_and_peace_ordenado.txt"]

def radix_sort(words):

    max_len = max(map(len, words))

    for i in range(max_len - 1, -1, -1):
        buckets = [[] for j in range(26)]
        for word in words:
            if len(word) > i:
                char = word[i]
                idx = ord(char) - ord('a')
                buckets[idx].append(word)
            else:
                buckets[0].append(word)
        words = [word for bucket in buckets for word in bucket]

    return words

def count_words(file_name, output):

    with open(file_name, 'r') as f:
        text = f.read().lower()
        words = re.findall(r'\b\w{4,}\b', text)
        words = [w for w in words if all(c in string.ascii_lowercase for c in w)]

    words = radix_sort(words)
    counter = Counter(words)

    with open(output, 'w') as f:
        for word, count in counter.items():
            f.write(f'{word} {count}\n')


#count_words(fileName[0], output[0])
#count_words(fileName[1], output[1])