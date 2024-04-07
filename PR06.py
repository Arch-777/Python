# Practical 6

# 1
x = {1, 2, 3, 'h'}
y = {1, 4, 5, 6}
a = x.intersection(y)
print(a)
b = x.union(y)
print(b)
c = x.difference(y)
print(c)
sym_diff = x.symmetric_difference(y)
print("The symmetric difference between set1 and set2 is:", sym_diff)
y.clear()
print(y)

# 2
s1 = {1, 2, 3, 4}
print(min(s1))
print(max(s1))

# 3
s1 = {1, 2, 3, 4, 5}
print(len(s1))
