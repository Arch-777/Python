def count_letters(text):
    uppercase_count = 0
    lowercase_count = 0
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    print("Lower case - ", lowercase_count)
    print("Upper case - ", uppercase_count)


count_letters("Hello World!c ")



