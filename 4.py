# increasing array

n=int(input())
x=list(map(int,input().strip().split(' ')))  # [6,10,4,10,2,8,9,2,7,7]  

c=0  # cursor
t=0  # turn
max=0  # temp max

for i in range(len(x)):
    if max<=x[i]:
        c=x[i]
        if c>max:
            max=c
        continue
    elif max>x[i]:
        #print('*',max-x[i])
        t=t+(max-x[i])
        #print(t)
        c=x[i]
        continue
    
print(t)