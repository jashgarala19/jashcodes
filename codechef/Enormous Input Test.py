n,k=input().split()
n=int(n)
k=int(k)
my_nums=[]
count=0
for i in range(n):
    my_nums.append(int(input()))

for i in range(len(my_nums)):
    if(my_nums[i]%k==0):
        count+=1

print(count)





