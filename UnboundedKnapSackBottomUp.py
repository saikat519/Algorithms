def unbounded(t,wt,val,cap,n):
    for i in range(n+1):
        for j in range(cap+1):
            if i==0 or j==0:
                t[i][j]=0

    for i in range(1,n+1):
        for j in range(1,cap+1):
            if j>=wt[i-1]:
                t[i][j]=max(val[i-1]+t[i][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]

    return t[n][cap]

val = [10,40,50,60]
wt = [1,3,4,5]
cap = 9
n=len(wt)
t=[[-1 for i in range(cap+1)]for j in range(len(wt)+1)]
print(unbounded(t,wt, val,cap,n))

