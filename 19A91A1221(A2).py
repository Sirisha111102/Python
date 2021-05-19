l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
for x in range(len(l1)):
    l3.append((l1[x],l2[x]))
print(l3)

"""OUTPUT:
1 2 3 4 5
6 7 8 9 10
[(1,6),(2,7),(3,8),(4,9),(5,10)]
"""
