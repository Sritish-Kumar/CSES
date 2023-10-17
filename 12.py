# Graay code

# Use binary no. XOR ----> Gray code

#(working)
n=int(input())
l=1
i=0

def gray(n):
    x=''                    # converting bin to gray
   
    x+=n[0]
    i=1
    while i<len(n):
        c=int(n[i]) ^ int(n[i-1])
        x+=str(c)
        i+=1
    return x


while l<=n:
    if len(bin(i)[2:])!=n:   # making the required len bin
        bn=(n-len(bin(i)[2:]))*'0'+bin(i)[2:]   
    else:
        bn=bin(i)[2:]
    gn=gray(bn)  # get gay
    print(gn)
    i+=1
    if len(bin(i)[2:])>l:       # len updating
        l=len(bin(i)[2:])
