# Creating Strings

import itertools

s=sorted(input())
rx=sorted(set(itertools.permutations(s)))
# tx=[]
# for i in list(rx):
#     if i not in tx:
#         tx.append(i)
# print(len(tx))
# for i in tx:
#     print(''.join(i))
#print(rx)
print(len(rx))
for i in rx:
    print(''.join(i))