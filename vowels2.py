#print the no of vowels in a string
s=input()
count=0
"""for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        count+=1
print("the no of vowels are:",count)"""
for i in s:
    if i in"aeiouAEIOU":
        count+=1
print("the no of vowels are:",count)
