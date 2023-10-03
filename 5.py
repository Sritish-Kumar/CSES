# Number spiral

rx=[]
c=1
rev=3
for i in range(1,10,2):
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



print(rx)

for i in range(len(rx)):
    zx=[]
    zx.append(rx[i].pop())
    x=ele()
    zx+=x
    print('*',zx)

    
