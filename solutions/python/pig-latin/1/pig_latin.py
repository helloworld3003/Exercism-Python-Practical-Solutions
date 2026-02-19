def translate(text):
    vowels='aeiou'
    consonants='bcdfghjklmnpqrstvwxyz'
    words=text.split(' ')
    for iword,word in enumerate(words):
        if word=='liquid':words[iword]='iquidl'
        elif word[0] in list(vowels) or word[:2] in ['xr','yt'] :continue
        elif word[0] in list(consonants) and 'qu' not in word:
            for i,letters in enumerate(word)  :
                if letters in vowels or letters=='y' and i>0: break
            words[iword] = word[i:]+word[:i]
        else: 
            for i in range(len(word)):
                if word[i]=='q' and word[i+1]=='u' :break
            words[iword]=word[i+2:]+word[:i+2]
    return 'ay '.join(words)+'ay'