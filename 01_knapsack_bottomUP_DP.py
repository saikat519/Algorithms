def knapsack(wt, val,W, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(wt, val,W, n))

'''
wt=[int(i) for i in input('weight of items :').split()]
val=[int(i) for i in input('Values of the items :').split()]
weight=int(input('Size of knapsack:::'))
n=len(wt)

# matrix dimention is variable parameters of recursive calls
# in this case n and weight is changing in each recursive calls
t=knapsack(wt,val,weight,n)
print('Total Profit:{}'.format(t[n][weight]))
'''