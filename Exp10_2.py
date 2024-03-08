"""import random
from math import floor, ceil

lower_bound = 5
upper_bound = 50
random_int = random.randint(floor(lower_bound), ceil(upper_bound) - 1)
random_float = random_int + random.random() * (upper_bound - lower_bound)

print(f"Generated random float: {random_float}")
"""


import random

# Generate a random float between 5 (inclusive) and 50 (exclusive)
random_float = random.uniform(5.0, 50.0)

print(f"Generated random float: {random_float}")