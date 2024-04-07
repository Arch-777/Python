# practical 4

# 1
li = [12, 23, 35, 44]
sum = 0
for x in range(0, 4):
    sum = sum + li[x]

print(sum)

# 2
li = [12, 23, 35, 44]
print(max(li))

# 3
li = [12, 23, 35, 44]
li.reverse()
print(li)


# 4
def common(list1, list2):
    return set(list1) & set(list2)


# Example usage
li1 = [1, 2, 3, 4, 5]
li2 = [3, 4, 5, 6, 7]

cn = common(li1, li2)

print("Common numbers:", cn)

# 5
li = [12, 23, 34, 45, 56]

for x in range(0, 5):
    if li[x] % 2 == 0:
        print("Even - ", li[x])
    else:
        continue
        