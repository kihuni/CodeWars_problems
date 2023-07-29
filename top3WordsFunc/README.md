Write a function that, given a string of text(possible with punctuation and line-breaks), returns an array of the top 3 most occuring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters(A to Z) optionally containing one or more apostrophes(') in ASCII.

Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)

Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.

Matches should be case-insensitive, and the words in the result should be lowercased.

Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

Examples:

```
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.

```

N/B Avoid sorting the entire array of unique words.

Solution:

In this [Example]() we are importing:
```
re: for reqular expression operations; to split text into words according to rules

collections: to count the occurrence of words

heapq: to keeo a running list if three most common words; for implemneting list based on regular lists

```
Next, we define a function `top_3_words` that takes `text` as an argument.
this function will find the three most common words in the provided text.

Next, we convert the text to lowercase using `text.lower()`, Then we use `re.findall` to split the text into words. The pattern `r"[a-z]+"`means one or more of any lower case letter `[a-z]` or apostrophe(')

next, we count the occurences of each words in the list `words` using `collection.Counter`, which returns a dictionary-like object; where keys are elements in  the list and values are their respective counts

next, We use heapq.nlargest to find the three most common words. The arguments to nlargest are:

3 - we want the three largest elements,
word_counts.keys() - the elements to consider are the keys of the word_counts dictionary (i.e., the words), and
key=word_counts.get - the comparison key is the count of each word, not the word itself. word_counts.get is a function that, given a word, returns its count.

Finally, we return `top_3`