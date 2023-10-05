# Trailing Zeros

n=int(input())
f=1
for i in range(2,n+1):
    f*=i
#print(f)
s=f'{f}'[::-1]
c=0
for i in s:
    if i=='0':
        c+=1
        continue
    else:
        break
print(c)

