import BCH

def syndrome_generator(bch,r): #r is little endian
    S=[]
    for i in range(0,2*bch.t+1):
        S.append([])
    S[0] = 0
    for i in range(1,2*bch.t):
        s=[]
        for a in range(0,2*bch.t+1):
            s.append(0)
        for a in range(0,2*bch.t+1):
            loc=(i*a)%(2**bch.m -1)
            s[loc]=r[a]
        S[i]=s
    return S