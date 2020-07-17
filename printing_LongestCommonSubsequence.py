def printlcs(t,a,b,m,n):
    # in this case no need to initialize matrix
    # Bcz I've already filled a matrix with 0 while creating  
    for i in range(1,m+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                t[i][j]=t[i-1][j-1]+1
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])

    i=m
    j=n
    ans=''
    while(i>0 and j>0):
        if a[i-1]==b[j-1]:
            ans+=a[i-1]
            i-=1
            j-=1
        else:
            if t[i-1][j] > t[i][j-1]:
                i-=1
            else:
                j-=1
    ans=ans[::-1]
    print(ans)

a='scgst'
b='sbcst'
m=len(a)
n=len(b)
t=[[0 for j in range(n+1)]for i in range(m+1)]
printlcs(t,a,b,m,n)
