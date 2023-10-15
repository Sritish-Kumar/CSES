# Graay code

# Use binary no. XOR ----> Gray code

#( Not working)
n=int(input())
l=1
i=0
c=0                         # all the bin value under the reqired len
while l<=n:
    if len(bin(i)[2:])!=n:
        print(i, (n-len(bin(i)[2:]))*'0'+bin(i)[2:])     
    else:
        print(i, bin(i)[2:])
    i+=1
    c+=1
    if len(bin(i)[2:])>l:
        l=len(bin(i)[2:])
    
#print(c)