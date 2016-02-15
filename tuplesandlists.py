Python 3.4.3 (default, Oct 14 2015, 20:28:29)
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> t = 4,7,9,12,45,78
>>> t
(4, 7, 9, 12, 45, 78)
>>> max(t)
78
>>> len(t)
6
>>> min(t)
4
>>> t[-1]
78
>>> type(t)
<class 'tuple'>
>>> y= [2,4,6,8,10,12,45]
>>> y
[2, 4, 6, 8, 10, 12, 45]
>>> type(y)
<class 'list'>
>>> y[8] = 9
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    y[8] = 9
IndexError: list assignment index out of range
>>> y
[2, 4, 6, 8, 10, 12, 45]
>>>
