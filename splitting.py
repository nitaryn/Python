Python 3.4.3 (default, Oct 14 2015, 20:28:29)
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>>
 s= 'this is a great day'

SyntaxError: unexpected indent
>>> s = 'This is a great day'
>>> s.split()
['This', 'is', 'a', 'great', 'day']
>>> words = s.split()
>>> words
['This', 'is', 'a', 'great', 'day']
>>> for w in words: print(w)

This
is
a
great
day
>>> new = ':'.join(words)
>>> new
'This:is:a:great:day'
>>> ','.join(words)
'This,is,a,great,day'
>>>
