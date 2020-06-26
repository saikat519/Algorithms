def knapsack(wt,val,t,capacity,n):
    if n == 0 or capacity == 0:
        return 0
    if t[n][capacity] != -1:
        return t[n][capacity]

    if wt[n - 1] <= capacity:
        t[n][capacity] = max(val[n - 1] + knapsack(wt, val,t, capacity - wt[n - 1], n - 1), knapsack(wt, val,t, capacity, n - 1))
        # max of by adding the item into the knapsack and BY not adding the item into knapsack
        # which one will give me the max profit
        return t[n][capacity]
    else:
        t[n][capacity] = knapsack(wt, val,t, capacity, n - 1)
        return t[n][capacity]

wt=[int(i) for i in input('Weight:').split()]
val=[int(i) for i in input('Values:').split()]
capacity=int(input('Enter Capacity::'))
n=len(wt)
t=[[-1 for i in range(1000)]for j in range(1000)]    # n and w will be given on problem
ans=knapsack(wt,val,t,capacity,n)
print("Max Profit will be :{}".format(t[n][capacity]))