n = int(input())
ls = list(map(int, input().split()))
sum = 0
for l in ls:
    sum += l
rsum = int((n*(n+1))/2)
print(rsum - sum)