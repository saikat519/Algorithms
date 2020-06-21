def fastpow(a,n):
    if n==0:
        return 1
    elif n%2==0:
        return fastpow(a*a,n/2)
    else:
        return a*fastpow(a,n-1)

print(fastpow(2,3))