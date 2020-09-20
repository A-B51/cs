l = []
l.append(2)
print(l)
l.append(5)
l.append(5)
print(l)

print(l[2])


def M(index):
    return(l[index - 1])

# print(M(0))
print(M(1))
print(M(2))

print(M(1) + M(2))
