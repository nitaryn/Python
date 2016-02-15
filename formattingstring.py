Python 3.4.3 (default, Oct 14 2015, 20:28:29)
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>>
a ,b =30, 45
>>> print(a,b)
30 45
>>> 'this is {},that is {}'
'this is {},that is {}'
>>> 'this is {},that is {}'.format(a,b)
'this is 30,that is 45'
>>> s = 'this is {},that is {}'
>>> s
'this is {},that is {}'
>>> s.format(a,b)
'this is 30,that is 45'
>>> id(s)
140228271503304
>>> 'this is {ann},that is {frank}'.format(ann=a,frank=b)
'this is 30,that is 45'
>>> d=dict(ann=a,frank=b)
>>> 'this is {ann},that is {frank}'.format(**d)
'this is 30,that is 45'
>>>
