# Digits
# Isnt working for larger numbers. 
# Isnt efficient. Try something other than strings. Mathmatecially calculating will work.

s=""
num=[]
r=int(input().strip())
for i in range(r):
    x=num.append(int(input()))

for i in range(1,max(num)):
    s+=f"{i}"

for i in (num):
    print(s[i-1])
