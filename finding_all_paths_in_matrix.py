def path(r,c):
    if r==1 or c==1:
        return 1
    else:
        return path(r,c-1)+path(r-1,c)

print(path(4,4))