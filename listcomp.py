l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for x in range(len(l1)):
    l3.append((l1[x],l2[x]))
print(l3)
