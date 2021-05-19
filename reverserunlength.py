s=input()
s1=""
for i in range(0,len(s),2):
    s1+=s[i]*int(s[i+1])
print(s1)
