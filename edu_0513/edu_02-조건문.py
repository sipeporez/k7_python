score = 83
if (90 <= score) and (score <= 100):
    print("A")
elif (80 <= score) and (score < 90):
    print("B")
elif (70 <= score) and (score < 80):
    print("C")
elif (60 <= score) and (score < 70):
    print("D")
else:
    print("F")


msg = "hello"
if msg == "hello":
    print("right")

data = []
if data:
    print("rigth!!!")

if 0:
    print("rigth!!!")

data = [1, 2, 3]
if 3 in data:
    print("contain")

string = "hello"
if "e" in string:
    print("contain")

print(sum([True, True, False]))


data = [1, 2, 3]
for d in data:
    if d < 3:
        print(d, end=" ")
    else:
        print("wrong!")
print("done!")
