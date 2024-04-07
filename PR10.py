# Practical 10

# 1
import numpy as np
mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

mat2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

add = mat1 + mat2
sub = mat1 - mat2
mul = mat1 * mat2
div = mat1 / mat2
print(add)
print(sub)
print(mul)
print(div)

# 2
import pandas as pd
string1 = "Hello, "
string2 = "world!"
concatenated_string = pd.Series([string1, string2]).str.cat()
print("Concatenated string:", concatenated_string)

# 3
import numpy as np
random_integers = np.random.randint(10, 31, size=6)
print("Six random integers between 10 and 30:", random_integers)