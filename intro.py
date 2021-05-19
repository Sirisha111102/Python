Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> a
5
>>> type(a)
<class 'int'>
>>> b=9.7
>>> b
9.7
>>> type(b)
<class 'float'>
>>> a="2ndit"
>>> a
'2ndit'
>>> tpe(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tpe(a)
NameError: name 'tpe' is not defined
>>> type(a)
<class 'str'>
>>> c="a"
>>> c
'a'
>>> type(c)
<class 'str'>
>>> d=True
>>> d
True
>>> type(d)
<class 'bool'>
>>> a=5
>>> b=5
>>> id(a)
1408215024
>>> id(b)
1408215024
>>> c=5
>>> d=8
>>> e=c+d
>>> c
5
>>> d
8
>>> e
13
>>> id(c)
1408215024
>>> id(d)
1408215072
>>> id(e)
1408215152
>>> a=6
>>> b=a
>>> a
6
>>> b
6
>>> id(a)
1408215040
>>> id(b)
1408215040
>>> type(a)
<class 'int'>
>>> "object polling"
'object polling'
>>> "REPL operations"
'REPL operations'
>>> a=3
>>> b=7
>>> a
3
>>> b
7
>>> "arthimetic operators"
'arthimetic operators'
>>> a
3
>>> a+b
10
>>> a-b
-4
>>> a*b
21
>>> a/b
0.42857142857142855
>>> a%b
3
>>> a//b
0
>>> a**b
2187
>>> a=5
>>> b=5
>>> id(a)
1408215024
>>> id(b)
1408215024
>>> b=6
>>> id(b)
1408215040
>>> c=7
>>> d=8
>>> c+d
15
>>> "expressions are also considered as objects in python"
'expressions are also considered as objects in python'
>>> type(c+d)
<class 'int'>
>>> id(c+d)
1408215184
>>> a,b,c=6,7,8
>>> a
6
>>> b
7
>>> c
8
>>> a,b,c=1,2.5,"it"
>>> a
1
>>> b
2.5
>>> c
'it'
>>> input()
4
'4'
>>> 'by default python interpreter prints the value as strings'
'by default python interpreter prints the value as strings'
>>> input("enter a number")
enter a number4
'4'
>>> "we have to convert into required data type we are using the constructors"
'we have to convert into required data type we are using the constructors'
>>> int('5')
5
>>> float('4.5')
4.5
>>> str(4)
'4'
>>> str(7.8)
'7.8'
>>> """int
float
str"""
'int\nfloat\nstr'
>>> int(input("enter a number:"))
enter a number:4
4
>>> float(input("enter a number:"))
enter a number:6.7
6.7
>>> a=int(input("enter a number:"))
enter a number:3
>>> a
3
>>> type(a)
<class 'int'>
>>> "in above int is a constructor of the specific classes but thy are not functions"
'in above int is a constructor of the specific classes but thy are not functions'
>>> "for output we are using the predefined function called print()"
'for output we are using the predefined function called print()'
>>> print(a)
3
>>> print(a,b)
3 2.5
>>> "when we are using comma by default it takes space between the two objects"
'when we are using comma by default it takes space between the two objects'
>>> print(a,b,sep=" ")
3 2.5
>>> print(a,b,sep="_")
3_2.5
>>> print(a,end=".")
3.
>>> print(a,end="\n",b)
SyntaxError: positional argument follows keyword argument
>>> " in any case positional argument follouws keyword argument"
' in any case positional argument follouws keyword argument'
>>> print(a,b,end="\n")
3 2.5
>>> "operators"
'operators'
>>> #siri
>>> """multi line comment"""
'multi line comment'
>>> """this isa line
multi line
comment"""
'this isa line\nmulti line\ncomment'
>>> '''hi
hello'''
'hi\nhello'
>>> """Arithemetic operators:+,-,*,/,%,//,**"""
'Arithemetic operators:+,-,*,/,%,//,**'
>>> a=5
>>> b=6
>>> a+b
11
>>> a-b
-1
>>> a*b
30
>>> a/b
0.8333333333333334
>>> a%b
5
>>> b%a
1
>>> a//b
0
>>> "floor division gives only the integer part value"
'floor division gives only the integer part value'
>>> a**b
15625
>>> "expoential performs the powe od and b values"
'expoential performs the powe od and b values'
>>> a=2
>>> b=3
>>> a**b
8
>>> """realational operators:<,>,<=,>=,==,!="""
'realational operators:<,>,<=,>=,==,!='
>>> "in this it returns only boolean values"
'in this it returns only boolean values'
>>> a=5
>>> b=6
>>> a<b
True
>>> a<=b
True
>>> a>b
False
>>> a>=b
False
>>> a==b
False
>>> a!=b
True
>>> a=5
>>> b='5'
>>> a==b
False
>>> "it checks the memory reference and datatype refrence also"
'it checks the memory reference and datatype refrence also'
>>> """logical opertaors:and,or,not"""
'logical opertaors:and,or,not'
>>> a=5
>>> b=4
>>> c=3
>>> a>b and a>c
True
>>> a<b or a>c
True
>>> not a
False
>>> """assignment operators:"""
'assignment operators:'
>>> a=5
>>> a=a+5
>>> a
10
>>> """if left hand side object is equal to right side first object"""
'if left hand side object is equal to right side first object'
>>> """Bitwise operators:&,|,~,^,<<,>>"""
'Bitwise operators:&,|,~,^,<<,>>'
>>> a=2
>>> b=3
>>> a&b
2
>>> a|b
3
>>> ~a
-3
>>> a^b
1
>>> a<<1
4
>>> a>>1
1
>>> """membership operators:in,not in"""
'membership operators:in,not in'
>>> "these operators are usd to check the whether are any object charcter space strings substrings in the given sequence"
'these operators are usd to check the whether are any object charcter space strings substrings in the given sequence'
>>> s="IT"
>>> "I" in s
True
>>> "i" in s
False
>>> "i" not in s
True
>>> " " in s
False
>>> "IT" in s
True
>>> """identity operators"""
'identity operators'
>>> "is is not"
'is is not'
>>> "these operators are used to check the datatype of atwo objects"
'these operators are used to check the datatype of atwo objects'
>>> a=5
>>> a='5'
>>> a is b
False
>>> a is not b
True
>>> c=5
>>> a is c
False
>>> """operators are concluded"""
'operators are concluded'
>>> 
