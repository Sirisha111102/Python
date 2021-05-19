Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,10):
	print(i,end=" ")

	
1 2 3 4 5 6 7 8 9 
>>> "by default the value is printed upto end-1"
'by default the value is printed upto end-1'
>>> for i in range(10):
	print(i,end=" ")

	
0 1 2 3 4 5 6 7 8 9 
>>> "by defalut without mentioing the starting value it takes 0 as starting value"
'by defalut without mentioing the starting value it takes 0 as starting value'
>>> for i in range(1,11,2):
	print(i,end=" ")

	
1 3 5 7 9 
>>> for i in range(10,0-1):
	print(1,end=" ")

	
>>> for i in range(10,0,-1):
	print(i,end=" ")

	
10 9 8 7 6 5 4 3 2 1 
>>> for i in range(10,0,-2):
	print(i,end=" ")

	
10 8 6 4 2 
>>> s="Python"
>>> for i in range(len(s)):
	print(s[i],end=" ")

	
P y t h o n 
>>> for i in range(len(s)):
	print(s[0])

	
P
P
P
P
P
P
>>> s="Python"
>>> for i in s:
	print(s[i],end=" ")

	
Traceback (most recent call last):
  File "<pyshell#30>", line 2, in <module>
    print(s[i],end=" ")
TypeError: string indices must be integers
>>> for i in s:
	print(i,end=" ")

	
P y t h o n 
>>> 
========= RESTART: C:/Users/sirisha/Documents/Python files/for-else.py =========
1 3 5 7 9 hurray!! task compleyed
>>> 
========= RESTART: C:/Users/sirisha/Documents/Python files/for-else.py =========
enter a name:sirisha
s i r i s h a finally task completed
>>> 
========= RESTART: C:/Users/sirisha/Documents/Python files/nestedfor.py ========
(1, 1),(1, 2),(1, 3),(1, 4),(1, 5),(1, 6),(1, 7),(1, 8),(1, 9),(1, 10),(2, 1),(2, 2),(2, 3),(2, 4),(2, 5),(2, 6),(2, 7),(2, 8),(2, 9),(2, 10),(3, 1),(3, 2),(3, 3),(3, 4),(3, 5),(3, 6),(3, 7),(3, 8),(3, 9),(3, 10),(4, 1),(4, 2),(4, 3),(4, 4),(4, 5),(4, 6),(4, 7),(4, 8),(4, 9),(4, 10),(5, 1),(5, 2),(5, 3),(5, 4),(5, 5),(5, 6),(5, 7),(5, 8),(5, 9),(5, 10),(6, 1),(6, 2),(6, 3),(6, 4),(6, 5),(6, 6),(6, 7),(6, 8),(6, 9),(6, 10),(7, 1),(7, 2),(7, 3),(7, 4),(7, 5),(7, 6),(7, 7),(7, 8),(7, 9),(7, 10),(8, 1),(8, 2),(8, 3),(8, 4),(8, 5),(8, 6),(8, 7),(8, 8),(8, 9),(8, 10),(9, 1),(9, 2),(9, 3),(9, 4),(9, 5),(9, 6),(9, 7),(9, 8),(9, 9),(9, 10),(10, 1),(10, 2),(10, 3),(10, 4),(10, 5),(10, 6),(10, 7),(10, 8),(10, 9),(10, 10),
>>> 
======= RESTART: C:/Users/sirisha/Documents/Python files/ritichie&riya.py ======

======= RESTART: C:/Users/sirisha/Documents/Python files/ritichie&riya.py ======
3 2 3
16
>>> 
============================================================= RESTART: C:/Users/sirisha/Documents/Python files/ritichie&riya.py ============================================================
4 3 4
28
>>> 
======== RESTART: C:/Users/sirisha/Documents/Python files/patternstar.py =======
how many lines to be printed:5
* * * * * * * * * * * * * * * 
>>> 
======== RESTART: C:/Users/sirisha/Documents/Python files/patternstar.py =======
how many lines to be printed:5
* 
* * 
* * * 
* * * * 
* * * * * 
>>> 
======== RESTART: C:/Users/sirisha/Documents/Python files/patternstar.py =======
how many lines to be printed:4
1 
2 2 
3 3 3 
4 4 4 4 
>>> 