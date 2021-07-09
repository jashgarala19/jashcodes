T=int(input())
all_test=[]
final_ans=[]
for i in range(T):
    all_test.append(input().split())

for i in range(T):
    a=int(all_test[i][0])%int(all_test[i][1])
    final_ans.append(a)

for i in final_ans:
    print(i)


