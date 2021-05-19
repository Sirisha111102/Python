#print lowercaseletters up to a range n
"""import string
s=int(input())
print(string.ascii_lowercase[:s])"""
s=int(input())
a=97
for i in range(s):
    print(chr(a),end="")
    a+=1
