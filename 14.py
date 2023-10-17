# Sets ( working )

num=[i for i in range(1, int(input())+1)]
num1=num

if sum(num)%2!=0:
    # odd
    print('NO')
else:
    # even

    req=sum(num)//2
    seta=[num.pop()]

    # Try adding elements to make it to the required number.

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

    print('YES')

    print(len(seta))
    print(' '.join(list(map(str,seta))), sum(seta))
    setb=set(num1)-set(seta)
    print(len(setb))
    print(' '.join(list(map(str, setb))), sum(setb))


    
