Python 3.4.3 (default, Oct 14 2015, 20:28:29)
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> s = "this is a string"
>>> s.capitalize()
'This is a string'
>>>
s.upper()
'THIS IS A STRING'
>>> s.swapcase()
'THIS IS A STRING'
>>> "THIS IS A STRING".swapcase
<built-in method swapcase of str object at 0x7fdd954ceae0>
>>> "THIS IS A STRING".swapcase()
'this is a string'
>>> 'this is a string'
'this is a string'
>>> s.find('a')
8
>>> 'this is awesome'
'this is awesome'
>>> s.replace('this','that')
'that is a string'
>>> id(s)
140589669345800


