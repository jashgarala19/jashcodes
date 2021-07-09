T=int(input())
triangles=[]
def check_valid(triangles):
  for i in range(len(triangles)):
    a=int(triangles[i][0])
    b=int(triangles[i][1])
    c=int(triangles[i][2])


    if(a+b+c==180):
        print('YES')

    else:
        print('NO')

for i in range(T):
 triangles.append(input().split())

check_valid(triangles)
