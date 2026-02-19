def translate(text):
    vowels='aeiou'
    vowels_y=vowels+'y'
    # consonants='bcdfghjklmnpqrstvwxyz'
    words=text.split(' ')
    for iword,word in enumerate(words):
        if word[0] in list(vowels) or word[:2] in ['xr','yt'] :continue
        else :
            for i,letters in enumerate(word)  :
                if (word[i:i+2] in 'qu') or (word[i] in vowels_y and i>0)   : break
            words[iword] = word[i:]+word[:i]
            word=words[iword]
            if 'qu' == word[:2] :
                    words[iword]=word[2:]+'qu'
    return 'ay '.join(words)+'ay'