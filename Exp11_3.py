def count_letters(text):
    uppercase_count = 0
    lowercase_count = 0
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return {
        "uppercase": uppercase_count,
        "lowercase": lowercase_count
    }


text = input("Enter a String - ")
letter_counts = count_letters(text)

print("Number of Uppercase Letters:", letter_counts["uppercase"])
print("Number of Lowercase Letters:", letter_counts["lowercase"])
