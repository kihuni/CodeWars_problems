import re
import collections
import heapq

def top_3_words(text):
    # Use regex to split the text into words, handling apostrophes as specified
    words = re.findall(r"\b[a-z]['a-z]*\b", text.lower())

    # Use collections.Counter to count occurrences of each word
    word_counts = collections.Counter(words)

    # Use heapq to find the three most common words
    top_3 = heapq.nlargest(3, word_counts.keys(), key=word_counts.get)

    return top_3

print(top_3_words("  //wont won't won't")) # ["won't", "wont"]