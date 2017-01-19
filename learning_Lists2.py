a = [1,2,-7,9,11]

print(a)

a[1] = "Hari's String"

print(a)

b = a
c = a[:]

print(c)

b[0] = 0

print a
print b
print c

a.append("new element")

print(a)
print(b)
print(c)
