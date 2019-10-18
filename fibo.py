(a, b) = (1, 2)
sum = 0
while b < 4000000 :
    if b % 2 is 0 : sum += b
    (a, b) = (b, a+b)
print(sum)
