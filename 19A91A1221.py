Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=2
>>> b=3
>>> a.__add__(b)
5
>>> a.__abs__()
2
>>> a.__and__(b)
2
>>> a.__eq__(b)
False
>>> a=2
>>> b=2
>>> a.__eq__(b)
True
>>> a.__float__()
2.0
>>> a=5
>>> b=4
>>> a.__floordiv__(b)
1
>>> a.__ge__(b)
True
>>> a__gt__(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a__gt__(b)
NameError: name 'a__gt__' is not defined
>>> a.__gt__(b)
True
>>> a=2.0
>>> a.__int__()
2
>>> a=2
>>> b=3
>>> a.__le__(b)
True
>>> a.__lshift__(b)
16
>>> a.__lshift__(1)
4
>>> b.__lt__(a)
False
>>> b.__mod__(a)
1
>>> a.__mul__(b)
6
>>> a.__ne__(b)
True
>>> b.__neg__()
-3
>>> a=4
>>> b=5
>>> a.__or__(b)
5
>>> a.__pos__()
4
>>> b.__pow__(a)
625
>>> a.__radd__(b)
9
>>> a.__rand__(b)
4
>>> a.__rfloordiv__(b)
1
>>> a.__rlshift__(1)
16
>>> a.__rmod__(b)
1
>>> a=6
>>> b=8
>>> a.__rmul__(b)
48
>>> a.__ror__(b)
14
>>> a.__rpow__(b)
262144
>>> a.__rrshift__(b)
0
>>> a.__rshift__(b)
0
>>> a.__rsub__(b)
2
>>> b.__rxor__(b)
0
>>> b.__rxor__(a)
14
>>> b.__str__()
'8'
>>> a.__sub__()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.__sub__()
TypeError: expected 1 argument, got 0
>>> a.__sub__(b)
-2
>>> b.__trunc__()
8
>>> a.__xor__(b)
14
>>> a=23.4556
>>> a.__trunc__()
23
>>> a=-9
>>> a.__abs__()
9
>>> """list of int class"""
'list of int class'
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 