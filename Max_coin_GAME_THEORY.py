def maxCoin(a,l,r):
    if l+1==r:
        return max(a[l],a[r])
    else:
        return max(a[l]+min(maxCoin(a,l+2,r),maxCoin(a,l+1,r-1)),
                   a[r]+min(maxCoin(a,l,r-2),maxCoin(a,l+1,r-1)))
a=[1,5,7,3,200,4]
r=len(a)-1
ans=maxCoin(a,0,r)
print('MAX profit will be::',ans)

'''
This kind of problem will not be solved with greedy method bcz greedy method tells about 
profit in each step but in this game 
for array [1,5,7,3,200,4]
in first step we can either choose a[0] or a[5] -----> game rule
so a[5] is greater 
in next step player B will choose max of a[0] and a[4]
so player B will win in his 1st step


in this problem we have to calculate how much profit i can gain
RULES::::
players can either choose 1st or last coin
'''