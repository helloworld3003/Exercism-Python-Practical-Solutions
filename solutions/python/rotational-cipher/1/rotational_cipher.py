def rotate(text, key):
    result = []
    for letter in text:
        if 'a' <= letter <= 'z':
            result.append(chr((ord(letter) - ord('a') + key) % 26 + ord('a')))
        elif 'A' <= letter <= 'Z':
            result.append(chr((ord(letter) - ord('A') + key) % 26 + ord('A')))
        else:
            result.append(letter)
    return ''.join(result)