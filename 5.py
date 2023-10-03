# Number spiral
# i couldnt make it more short. A wise man once said if your code is smaller and works fine then that is the best code. 
# I know that, I gave it try and i just made it somehow work. It works but with the expense of time and memory. 

rx=[]
c=1
rev=3
for i in range(1,24,2):
    l=[]
    for j in range(i):       # ------------ making the diagonal stretched element
        #print(c)
        l.append(c)
        c+=1
    if (i-rev)==0:
        l.sort(reverse=True)
        rev+=4
    rx.append(l)    
    #print()
#print(rx)

tx=[]               # ----------- makking the matrix


def ele():
    global rx
    
    x=[]
    for i in rx:
        
        try:
            x.append(i.pop())
        except:
            continue
    return x



#* print(rx)

for i in range(len(rx)):
    zx=[]
    t=0
    while True:
        try:
            zx.append(rx[i].pop(t))
        except:
            break
    #zx=zx[::-1]

    x=ele()
    zx+=x
    #* print('*',zx)
    tx.append(zx)
#* print(tx)

n=int(input())
out=[]
for i in range(n):
    r1,*c1=list(map(int,input().strip().split(' ')))
    c1=c1[0]
    out.append(tx[r1-1][c1-1])
for i in out:
    print(i)


