# 4-3
for i in range(1, 21):
    print(i, end=" ")
print()

# 4-4
number = list(range(1, 1000001))
# for i in number:
#     print(i)

# 4-5
print(min(number))
print(max(number))
print(sum(number))

# 4-6
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# 4-7
for i in range(3, 31, 3):
    print(i, end=" ")
print()

# 4-8
for i in range(1, 11):
    print(i**3, end=" ")
print()

# 4-9
comprehension = [i**3 for i in range(1, 11)]
print(comprehension)
