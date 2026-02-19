def is_valid(isbn):
    
    isbn=list(isbn.replace('-',''));t=0;k=0
    if len(isbn)==10:
        if isbn[len(isbn)-1]=='X':isbn[len(isbn)-1]='10' 
        for i,l in enumerate(isbn):
            if not l.isdigit():l=0;k=1
            t+=int(l)*(10-i)
    return t%11==0 and len(isbn)==10 and k!=1
