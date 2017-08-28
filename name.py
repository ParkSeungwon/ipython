age = 20
name = 'ParkSeungwon'
print age
print name
print '%s am %.3f years old'%(name, age)
print \
age, name
for i in range(1, 5):
    print i
    
else : print 'over'
x=10
def f():
    global x
    print x
    
f()

import sys
for i in sys.argv:
    print i
   
from sys import path 
for i in path:
    print i
