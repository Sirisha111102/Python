s=input()
l=0
u=0
d=0
sy=0
for i in s:
    if i.islower():
        l+=1
    elif i.isupper():
        u+=1
    elif i.isdigit():
        d+=1
    else:
        sy+=1
if(l==u==d==sy):
    print("Equality for everyone")
else:
    print("no equality")
