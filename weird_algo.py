n = int(input())
print(int(n),end=" ")
while(n!=1):
    if n%2==0:
        n /= 2
        print(int(n),end=" ")
    else:
        n = (n*3)+1
        print(int(n), end=" ")