a = [[1, 2],[2,3],[3,4]]
print(a)


b = []

for x in range(len(a)):
    b.append([])
    for y in range(len(a[x])):
        b[x].append(a[x][y])

print(b)
print(a)
