from collections import Counter

d1 = {'9': 200, 'b': 200, 'c': 300}
d2 = {'9': 300,  'b': 200, 'd': 400}
d3 = Counter(d1) + Counter(d2)
print(d3)
