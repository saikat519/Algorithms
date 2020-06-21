sett=set()
def permutation(s,l,r):
    if l==r:
        if s in sett:
            return   #coz set gives unique value if we didn't use set for abcc it will contain dublicate vals
        sett.add(s)
        print(s)
        return
    else:
        for i in range(l,r+1):
            s=InterchangeChar(s,l,i)
            permutation(s,l+1,r)
            s=InterchangeChar(s,l,i)
def InterchangeChar(s,a,b):
    s=list(s)
    s[a],s[b]=s[b],s[a]
    s=''.join(s)
    return s


permutation('abcc',0,3)