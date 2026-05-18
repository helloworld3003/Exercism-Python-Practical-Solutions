def rows(letter):
    l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    re=[]
    d={a:i for i,a in enumerate(l)}
    letter=letter.upper()
    n=d[letter]
    if (letter=="A"): return list("A")
    else:
        for i in range(2*n+1):
            r=""
            for j in range(abs(n-i)): 
                r+=(" ")
            r+=(l[i]) if(i<=n) else (l[2*n-i])
            x=1 if (i==0 or i==(2*n)) else 2
            for j in range(2*n-2*abs(n-i)-x+1):
                r+=(" ")
            if (x==2):
                r+=(l[i]) if(i<=n) else (l[2*n-i])
            for j in range(abs(n-i)): 
                r+=(" ")
            re.append(r)
    return re