T=int(input())
fact=[]

def get_fact(num):
   sum = 1
   for i in range(1,num+1):
       sum=sum*i

   return sum
def find_facts(fact):
    for i in range(len(fact)):
        num = int(fact[i])
        a = get_fact(num)
        print(a)



for i in range(T):
    fact.append((input()))

find_facts(fact)

