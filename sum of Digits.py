T=int(input())
n=[]

def get_sum(number):
    sum=0

    temp = number
    for i in str(number):
        sum = sum + (temp%10)
        temp=temp//10
    print(sum)
    return


for i in range(T):
    n.append(int(input()))

for i in range(T):
    get_sum(n[i])


