from heapq import nlargest
d = {1: 20, 2: 30, 3: 40, 4: 50}
t = nlargest(3, d)
print(t)
