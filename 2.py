#Missing Number
n=int(input().strip())
l=list(map(int, input().strip().split(' ')))

n=[i for i in range(1,n+1)]

print(sum(n)-sum(l))