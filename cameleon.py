v = [] 
end = False
def Cameleon(a, b, c) :
    if end is True : return
    k = 0
    if a is 0: k += 1
    if b is 0: k += 1
    if c is 0: k += 1
    if k is 2:
        print 'changed to one color'
        end = True
        return
    if a<0 or b<0 or c<0: return

    ar = [a,b,c]
    if ar in v: return
    else: v.append(ar)

    Cameleon(a-1, b-1, c+2)
    Cameleon(a+2, b-1, c-1)
    Cameleon(a-1, b+2, c-1)
print 'first case'
end = False
Cameleon(1,3,5)
end = False
print 'second case'
Cameleon(37, 61, 27)
