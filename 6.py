# Permutation
# this is a stupid code. U dont need to do this much labour. I was stupid to try this.
# Use u r brain and try to seperate the odd and even part and stick them side to side
#Like [1,2,3,4,5]------> [2,4,1,3,5]

n=int(input())

if n in [0,2,3]:
    print('NO SOLUTION')
else:

    out=[]
    i=1
    rev=0
    
    if n%2==0:
        #print('Even')

        echk=int(n/2)
        echk=[echk,echk+1]
        #print(echk)

        while True:
            if i in echk and n in echk:
                out.insert(0,echk.pop())
                out.append(echk.pop())
                break

            if rev==0:
                out.append(i)
                rev=1
                i+=1
            elif rev==1:
                out.append(n)
                n-=1
                rev=0

    else:
        #print('Odd')
        ochk=int((n+1)/2)
        #print(ochk)

        while True:

            if i==ochk and n==ochk:
                out.insert(0,ochk)
                break
                
            elif rev==0:
                out.append(i)
                i+=1
                rev=1
                    
            elif rev==1:
                out.append(n)
                n-=1
                rev=0

    

    for i in out:
        print(i, end=' ')
