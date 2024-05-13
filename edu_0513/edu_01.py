data = [1, 2, 3]

for d in data:
    print(d, end=" ")

string = "hello"

for s in string:
    print(s, end=" ")


data = (4, 5, 6)
for i in data:
    print(i)

data2 = [i**2 for i in data]
print(data2, type(data2))

data3 = []
for i in data:
    data3.append(i**2)
print(data3)
