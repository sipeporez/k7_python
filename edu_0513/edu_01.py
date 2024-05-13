data = [1, 2, 3]

for d in data:
    print(d, end=" ")

string = "hello"

for s in string:
    print(s, end=" ")


data = (1, 2, 3)
for i in data:
    print(i)

data2 = [i**2 for i in data if i**2 < 5]
print(data2, type(data2))

data3 = []
for i in data:
    if i**2 < 5:
        data3.append(i**2)
print(data3)


data = [1, 2, 3, 4, 5]

for d in data:
    print(d)

for idx, d in enumerate(data):
    print(idx, d)


data_2d = [[1, 2, 3], [4, 5, 6]]
for data in data_2d:
    for d in data:
        print(d, end=" ")
    print()


for data in range(1, 10):
    for d in range(1, 10):
        # print(data, "*", d, "=", d * data)
        print(f"{data} X {d} = {data*d}")
    print()

totalsum = 0
for i in range(1, 11):
    totalsum += i
print(totalsum)

print(sum(range(1, 11)))
print(min(range(1, 11)))
print(max(range(1, 11)))
print(sum(range(1, 11)) / len(range(1, 11)))

data = list(range(2, 1001, 2))
for d in data:
    print(d, end=" ")
