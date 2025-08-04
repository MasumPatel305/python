sample_words = ["python", "dictionary", "loop", "function"]

def word_lengths(words):
    return {word: len(word) for word in words}

print(word_lengths(sample_words))
