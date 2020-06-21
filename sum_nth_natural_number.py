def nat(n):
    if n==1:
        return 1
    else:
        return nat(n-1)+n

    
n=int(input('Range:'))
print(nat(n))