# 10. Function to compute frequency of words in a string
def word_frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
