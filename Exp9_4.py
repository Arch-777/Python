data = [{"v": "3001"}, {"v": "3002"}, {"vi": "3001"}, {"v": "3003"}, {"vii": "3007"}]

# Method 1: Using set comprehension with error handling
unique_values = {item.get("v") for item in data if isinstance(item.get("v"), str)}
print("Union of dictionary values (Strict approach, string values only):", unique_values)

# Method 2: Using loop and set with error handling
unique_values = set()
for item in data:
    value = item.get("v", "NA")  # Handle missing or non-string values with "NA"
    unique_values.add(value)
print("Union of dictionary values (Flexible approach, including non-string values):", unique_values)
