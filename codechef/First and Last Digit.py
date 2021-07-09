T=int(input())
mynums=[]
finalnums=[]

for i in range(T):
    mynums.append(input())

for i in range(T):
    str_len=len(mynums[i])
    a=mynums[i][0]
    b=mynums[i][str_len-1]
    finalnums.append(int(a)+int(b))

for i in finalnums:
    print(i)
