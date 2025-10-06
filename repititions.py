s = str(input())
ls = list(s)
cr = 1 #to count
temp = 1 #to temporary store the max count
for i in range(len(ls)-1):
    c = ls[0]
    if ls[i]==ls[i+1]:
        cr += 1
        if cr>temp:
            temp = cr 
    else:
        cr = 1
        c = ls[i]
    
print(temp)

