marks = [97, 15, 41, "Python"]
print(marks)
marks.append(59)
marks.insert(0, 12)
# -1 indicates that it will print index from right to left
# 0 shows it will print from left to right
for score in marks:
    print(score)
print(15 in marks)
print(len(marks))
marks.clear()
print(marks)
