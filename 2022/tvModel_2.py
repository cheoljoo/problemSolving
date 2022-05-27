N = 4
Y = [(-15, 10), (-10, 20), (10, 15), (15, 100)]

Y.sort()
e = Y[0][1]
sol = 1
for i in range(1, N):
    if Y[i][0] > e:
        sol += 1
        e = Y[i][1]
    if Y[i][1] < e:
        e = Y[i][1]

print(sol)