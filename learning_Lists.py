a = [1, -7, 0, 0, 5, 10]

print(a[0])

print(a[2])

a[4] = "this text"

print(a)

a[0] = [-1, -2]

print(a)

b = [7, 7, 13, 15]

c = b # c and b are pointing to the same info in memory, if we change c we also change b. THIS DOES NOT COPY b

c[0] = 1

print(c)
print(b[0])

c = b[:] # This is how you actually make a copy of a list
c = b[0:2] # This is UP TO BUT NOT INCLUDING THE 2ND ELEMENT

print(c)