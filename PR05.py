# Practical 5

# 1
t1 = (12, 23, 34, 45, 56)
print(min(t1))
print(max(t1))

# 2
def find_repeated_numbers(my_tuple):
  return [num for num in my_tuple if num in set(my_tuple) and my_tuple.count(num) > 1]


# Example usage
my_tuple = (1, 2, 3, 2, 4, 5)

repeated_numbers = find_repeated_numbers(my_tuple)

if repeated_numbers:
  print("Repeated numbers:", repeated_numbers)
else:
  print("No repeated numbers found")

# 3
s1 = {1, 2, 3, 4, 5}
print(s1)
s1.add('s')
print(s1)
s1.remove(5)
print(s1)

# 4
def find_highest_three(my_dict):
  return sorted(my_dict.values(), reverse=True)[:3]


my_dict = {'a': 100, 'b': 200, 'c': 50, 'd': 150, 'e': 300}

highest_three = find_highest_three(my_dict)

print("Highest 3 values:", highest_three)