import pandas as pd
string1 = "Hello, "
string2 = "world!"
concatenated_string = pd.Series([string1, string2]).str.cat()
print("Concatenated string:", concatenated_string)
