msg = "hello, world!"

print(msg.title(), type(msg))

print(msg.capitalize())

print(msg.find("l"))

print(msg[0])
print(msg[1])
print(msg[0:3])

a = "hello"
b = "world"


def add(a, b):
    return a + b


print(f"{a}, {b}!, {add(1,2)} \nasdfas\tfasfa")

msg = "     hello    "
print(len(msg))
print(msg.lstrip())
print(len(msg.rstrip().lstrip()))
msg = msg.strip()
print(msg)

msg = "hello, hello, hello, world!"
print(msg.replace("hello", "Hi"))
print(msg.replace("hello", "Hi").replace("Hi", "").replace(",", "").strip())
