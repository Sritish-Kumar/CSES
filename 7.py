# Trailing Zeros
# The calculation works fine. Just takes time for larger numbers. 
# Would reccomand the calculation method. Just try to optimize it more. 

import time
start=time.time()
n=int(input())
f=1
for i in range(2,n+1):
    f*=i
    
#print(f)
'''s=f'{f}'[::-1]
c=0                     # string method
for i in s:
    if i=='0':
        c+=1
        continue
    else:
        break
print(c)'''
c=0                 # calculation method
h=10
while True:
    if f%h==0:
        c+=1
        h*=10
        #f=int(f/h)
        continue
    else:
        break
print(c)
print(time.time()-start)


# ------------- > working

n=int(input().strip())
i=5
c=0
while True:
    if n//i==0:
        break
    #print(n,i,c)
    c+=n//i
    i*=5
    
    
print(c)


