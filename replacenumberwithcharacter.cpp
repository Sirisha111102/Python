s=input()
s1=""
for i in range(0,len(s),2):
    s1+=s[i]
    s1+=chr(((ord(s[i])-ord('a'))+(ord(s[i+1])-ord('0')))%26+97)
print(s1)
