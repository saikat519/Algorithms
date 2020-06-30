def unbounded(t,wt,val,cap,n):
    if n==0 or cap==0:
        return 0
    if t[n][cap]!=-1:
        return t[n][cap]
    if wt[n-1] <= cap:
        t[n][cap]=max(val[n-1]+unbounded(t,wt,val,cap-wt[n-1],n),unbounded(t,wt,val,cap,n-1))
        return t[n][cap]
    else:
        t[n][cap]=unbounded(t,wt,val,cap,n-1)
        return t[n][cap]

val = [10,40,50,60]
wt = [1,3,4,5]
cap = 9
n=len(wt)
t=[[-1 for i in range(cap+1)]for j in range(len(wt)+1)]
print(unbounded(t,wt, val,cap,n))

