T=int(input())
choices=[]
class Ship:
    b='BattleShip'
    c='Cruiser'
    d='Destroyer'
    f='Frigate'

op=Ship()

for i in range(T):
    choices.append(input())

for i in range(len(choices)):
    if(choices[i]=='B' or choices[i]=='b'):
        print(op.b)
    elif(choices[i]=='c' or choices[i]=='C'):
        print(op.c)
    elif(choices[i]=='d' or choices[i]=='D'):
        print(op.d)
    elif(choices[i]=='f' or choices[i]=='F'):
        print(op.f)


