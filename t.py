import random
x = -2
if x > 0 :
    print 'positive'
elif x > -3 :
    print 'mi'
else :
    print 'negative'

for i in range(10):
    print random.random()
    print random.randint(3, 12)

while True:
    break
def f(values):
    for v in values:
        print v

f([2,3,4])
f('fdfd')

f_name = raw_input('type filename : ')
try:
    fh = open(f_name)
except:
    print 'not opened', f_name

for l in fh:
    print l.rstrip()

fh.close()

