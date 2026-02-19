def is_pangram(sentence):
    letters=list(map(chr,range(97,123)))
    return all(i in sentence.lower() for i in letters)