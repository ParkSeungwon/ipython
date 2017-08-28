c = [25, 20, 10, 5, 1]
co = [0] * 5
M = 40
i = 0
while M > 0 : 
    while c[i] <= M :
        M -= c[i]
        co[i] += 1
    i += 1
print co
