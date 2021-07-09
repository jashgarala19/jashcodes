T=int(input())
all_case=[]
final_case=[]
for i in range(T):
  all_case.append(input().split())
for i in range(T):
    final_case.append(int(all_case[i][0])+int(all_case[i][1]))
for i in final_case:
    print(i)




