a,b,n=map(int,input().split())#3 2 3
for i in range(n):
    if i%2==0:
        a*=2
    else:
        b*=2
print(a+b)
        
