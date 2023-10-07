# Creating Strings
# Time limit exceed for larger numbers. Other than that works fine
import itertools

s=sorted(input())
rx=itertools.permutations(s)
tx=[]
for i in list(rx):
    if i not in tx:
        tx.append(i)
print(len(tx))
for i in tx:
    print(''.join(i))
