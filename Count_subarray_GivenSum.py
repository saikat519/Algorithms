def count_subarray(n,arr,given_sum,t):
    for i in range(n+1):
        for j in range(given_sum+1):        # initialize matrix
            if i==0:
                t[i][j]=0
            if j==0:
                t[i][j]=1



    for i in range(1,n + 1):
        for j in range(1,given_sum + 1):
            if j>=arr[i-1]:
                t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
            else:
                t[i][j] =t[i-1][j]
    return t[n][given_sum]



arr=[2,3,4,4,5,10,5]
n=len(arr)
given_sum=10
t=[[-1 for i in range(given_sum+1)]for j in range(n+1)]
ans=count_subarray(n,arr,given_sum,t)
print(ans)


'''
initialization part:::

if sum is given and array is not given it is not possible to make a subset from there so mark 0

if array elements are given but sum is 0
then it is possible of empty subarray so mark 1
AFter initialization array t should look like this

[1,0,0,0,0,0,0,0,0,0 ]                  
[1,                  ]
[1,                  ]
[1,                  ]
[1,                  ]
[1,                  ]



'''