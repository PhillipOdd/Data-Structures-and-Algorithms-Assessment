import string

def word_frequency(sentence):
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Tokenize the sentence into words
    words = sentence.split()

    # Define a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    for word in words:
        # Remove punctuation and convert to lowercase
        clean_word = word.translate(translator).lower()

        # Update word frequency in the dictionary
        if clean_word in word_freq:
            word_freq[clean_word] += 1
        else:
            word_freq[clean_word] = 1

    return word_freq
