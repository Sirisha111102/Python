n=int(input())
b=0
for i in range(n,0,-1):
    b+=1
    for j in range(i+1):
        print(j,end=" ")
        #b+=1
    print()
