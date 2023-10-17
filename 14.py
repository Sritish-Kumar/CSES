# Two Sets ( working )


# Works fine
# Principal: If the sum of numbers is odd not possible to divide it into 2 set
# If sum is even may be divided
# Now if the sum is even. Try making each set as n//2. 


num=[i for i in range(1, int(input())+1)]
num1=num

if sum(num)%2!=0:
    # odd
    print('NO')
else:
    # even

    req=sum(num)//2     # Required sum 
    x=num.pop()
    seta=[x]

    def check(num):
        global seta
        for i in num:
            if i+sum(seta) == req:
                seta.append(i)
                break
            elif i+sum(seta) < req:
                seta.append(i)
                if req-sum(seta) in num and req-sum(seta)!=i:
            
                    seta.append(req-sum(seta))
                    break
                continue

            elif i + sum(seta)> req:
                continue
    check(num)                      # checking from smaller to bigger 
    setb=set(num1)-set(seta)
    if sum(seta)==sum(setb):
        None
        # print('YES')

        # print(len(seta))
        # print(' '.join(list(map(str,seta))))
        
        # print(len(setb))
        # print(' '.join(list(map(str, setb))))
    else:
        seta.clear()
        
        seta=[x]
        setb.clear()
        check(sorted(num,reverse=True))     # If not found checking from bigger to smaller
        setb=set(num1)-set(seta)
        # print('YES')
        # print(len(seta))
        # print(' '.join(list(map(str,seta))))
        
        # print(len(setb))
        # print(' '.join(list(map(str, setb))))
    print('YES')

    print(len(seta))
    print(' '.join(list(map(str,seta))))
        
    print(len(setb))
    print(' '.join(list(map(str, setb))))