def is_isogram(string):
    string = ''.join(string.lower().replace('-',' ').split())
    return string==''.join(dict.fromkeys(string))
