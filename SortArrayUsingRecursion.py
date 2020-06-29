def sortstk(stk):
    if len(stk)==0:
        return
    if len(stk)!=0:
        temp=stk.pop()
        sortstk(stk)
        insertstk(temp,stk)

def insertstk(temp,stk):
    if len(stk)==0 or stk[-1]<temp:
        stk.append(temp)
        return
    else:
        t=stk.pop()
        insertstk(temp,stk)
        stk.append(t)


stk=[3,7,12,4]
sortstk(stk)
for i in stk[::-1]:
    print(i,end=' ')