def productArray(a,n):

    left=[0]*n       #initializing arrays with 0's
    right=[0]*n
    product=[0]*n

    left[0]=1         # left=[1,0,0,0]

    right[n-1]=1      # right=[0,0,0,1]

    for i in range(1,n):
        left[i]=left[i-1]*a[i-1]      # initially left=[1,0,0,0] so we have to start from 2nd position

    for j in range(n-2,-1,-1):
        right[j]=right[j+1]*a[j+1]  # initially right=[0,0,0,1] so we have to start from 2nd last position

    for k in range(n):
        product[k]=left[k]*right[k]

    print(product)


a=[1,2,3,4]
n=len(a)
productArray(a,n)

'''
Given an array a[] of n integers, construct a Product Array prod[] (of same size) 
such that prod[i] is equal to the product of all the elements of a[] except a[i]

e.g:-

Input: arr[]  = {10, 3, 5, 6, 2}
Output: prod[]  = {180, 600, 360, 300, 900}
                    
'''