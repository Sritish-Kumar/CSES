# Plaindome re-order
# ponits: 2 odd numebrs wont work
# Works  fine


import collections

s=input().strip()
l=dict(collections.Counter(s))          # If any two letter are in odd number you can't arrange them  in plaindome
c=0
for i in l.values():
    if i%2==0:
        continue
    else:
        c+=1
#print(l)
if c>1:
    print('NO SOLUTION')

else:
    rx=[]
    tx=[]
    od=[]
    for i in l:
        #print(i)
        if l[i]%2==0:
            # even
            rx.append(i*int(l[i]/2))
            tx.append(i*int(l[i]/2))
        else:
            # odd
            rx.append(i*int(l[i]/2))
            tx.append(i*int(l[i]/2))
            od.append(i*1)
            
    print(''.join(rx+od),end='')
    print(''.join(tx[::-1]))
