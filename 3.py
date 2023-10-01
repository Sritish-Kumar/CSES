#Repetition
# 

s=input().strip()#'ATTCGGGA'
c=''
l=''
max=0
count=0

for i in s:
    
    if c==i:
        count+=1

        if max<=count:
            
            l=i
            max=count
    elif c!=i:
        count=0        
    c=i
#print(l*(max+1), max+1)
print(max+1)