def sub_arr(arr,n,s,t):
    for i in range(n+1):
        t[i][0]=True
    for j in range(1,s+1):
        t[0][j]=False
    for i in range(n+1):
        for j in range(s+1):
            if j>=arr[i-1]:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]




arr=[11,7,3,4]
n=len(arr)
max_range=sum(arr)
t=[[False for i in range(max_range+1)]for j in range(n+1)]
sub_arr(arr,n,max_range,t)
diff=999999
for j in range(max_range//2,-1,-1):     # vector concept
    if t[n][j]==True:
        diff=min(diff,max_range-2*j)

print(diff)


'''
so basically we are working with last row of t[i][j] i---->number of element j--->sum of that range

 if we got sum of s1 then no need to calculate sum of s2 right?
 max_range is maximum sum difference of subsets which is
  difference  between {empty set sum}=0 and whole set given {11,7,3,4}=25 
MAXIMUM diff is 25-0=25 so range is 0 to 25  

Now from t[][] last row(nth) we know that which subsetSUM is possible by true and false  

so if t[n][j]==True   ---> subsetSum is possible
        diff= sum_arr - 2*j  ----> minimization of sum(arr)-2s1

'''