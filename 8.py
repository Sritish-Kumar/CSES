# Bit strings. 
# Time limit will exceed in cses. If u try the experimental value 2**n
# It works fine upto a certain value. After that i think the sequence changes or something like that. It will give u wrong ans. 

n=int(input())
'''l=1
i=0
c=0                         # all the bin value under the reqired len
while l<=n:
    print(i,bin(i)[2:])     
    i+=1
    c+=1
    if len(bin(i)[2:])>l:
        l=len(bin(i)[2:])
print(c)'''

print(2**n)         # experimentally found
