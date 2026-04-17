abc='abcdefghijklmnopqrstuvwxyz'
rev={abc[i]: abc[25-i] for i in range(26)}

def encode(plain_text):
    encoded=""
    j=0
    joined=plain_text.replace(",","").replace(" ","").replace(".","").lower()
    for letters in joined:
        j+=1
        encoded=encoded+rev[letters] if letters in abc else encoded+letters
        encoded=encoded+" " if j%5==0 else encoded
    return encoded if encoded[-1]!=" " else encoded[:-1]


def decode(ciphered_text):
    decoded=""
    joined=ciphered_text.replace(" ","")
    for letters in joined:
        decoded=decoded+rev[letters] if letters in abc else decoded+letters
    return decoded